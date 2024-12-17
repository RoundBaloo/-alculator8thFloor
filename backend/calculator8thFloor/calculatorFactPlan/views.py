from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import FactDataSerializer, PlanDataSerializer, InputedFieldsDataSerializer, UserSerializer, ChangePasswordSerializer, GetTableColumnNamesSerializer
from .models import Data, TableColumnName
from drf_yasg.utils import swagger_auto_schema
from .components.data_updater import DataUpdater
import json
from django.http import FileResponse
import xlsxwriter
from docxtpl import DocxTemplate
from .components import export_functions, fill_columns_names
from spire.doc import *
from spire.doc.common import *
from django.shortcuts import render
import requests
# Create your views here.


class FactDataViewSet(ListModelMixin, GenericViewSet):
    queryset = Data.objects.all()
    serializer_class = FactDataSerializer
    http_method_names = ['get']

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Передает данные для таблицы Факта",
                         operation_description="Возвращает список словарей. \
                                Каждый словарь - отдельная строка в таблице. \
                                    Ключ - название столбца из модели, значение - вычисленное значение",
                         tags=["Fact Data"])
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = Response(serializer.data)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok
        return response


class PlanDataViewSet(ListModelMixin, GenericViewSet):
    queryset = Data.objects.all()
    serializer_class = PlanDataSerializer

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Передает данные для таблицы Плана",
                         operation_description="Возвращает список словарей. \
                                Каждый словарь - отдельная строка в таблице. \
                                    Ключ - название столбца из модели, значение - вычисленное значение",
                         tags=["Plan Data"])
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = Response(serializer.data)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok
        return response


class InputedDataViewSet (ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Data.objects.all()
    serializer_class = InputedFieldsDataSerializer

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Передает вводимые данные",
                         operation_description="Возвращает данные, которые заполняют поля для ввода. \
                                 Эти данные используются для упрощения пользования приложением, \
                                 например, чтобы по новой не вводить кол-во машин заново каждый раз.",
                         tags=["Input Data"])
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = Response(serializer.data)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok
        return response

    @swagger_auto_schema(operation_summary="Получает и обрабатывает данные",
                         operation_description="Получает введенные данные и на их основе пересчитывает \
                             все вычисляемые значения.\
                             avg_fact_files_per_month переданный для 180h_day применяется и для 168h; 79h.",
                         tags=["Input Data"])
    def create(self, request, *args, **kwargs):
        data = json.loads(request.GET.get('data'))
        if (
            data['cnt_machines']['180h'] <= 0
            or data['cnt_machines']['168h'] < 0
            or data['cnt_machines']['79h'] < 0
            or data['avg_fact_files_per_month']['180h_day'] < 0
            or data['avg_fact_files_per_month']['168h'] < 0
            or data['avg_fact_files_per_month']['79h'] < 0
            or data['avg_fact_files_per_month']['180h_weekend'] < 0
            or data['avg_fact_files_per_month']['180h_night'] < 0
            or data['cnt_UZ'] < 0
            or data['permitted_load'] < 0
        ):
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
        table = request.GET.get('table')
        data_updater = DataUpdater(data)
        data_updater.handle_inputed_data(table)

        response = Response({"message": "All Data objects have been updated"}, status=status.HTTP_200_OK)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok

        return response


class HeadViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Передает список всех пользователей приложения",
                         tags=["Head features"])
    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = Response(serializer.data)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok

        return response

    @swagger_auto_schema(operation_summary="Создает новых пользователей",
                         tags=["Head features"])
    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Проверка на наличие обязательных полей
        if not email or not password or not username:
            response = Response({"error": "required fields are not filled in"}, status=status.HTTP_400_BAD_REQUEST)
            response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok
            return response
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            response = Response({"message": "User  created successfully.", "user_id": user.id}, status=status.HTTP_201_CREATED)
            response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok
            print('success')
            return response
        except Exception as e:
            print('error')
            response = Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok
            return response

    @swagger_auto_schema(operation_summary="Удаляет пользователей",
                         tags=["Head features"])
    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"error": "У вас нет прав на удаление пользователей"}, status=status.HTTP_403_FORBIDDEN)

        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Пользователь успешно удален"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Обновляет пароль пользователю",
                         tags=["Head features"])
    def update(self, request, pk=None, partial=False):
        if not request.user.is_superuser:
            return Response({"error": "У вас нет прав на изменение пользователей"}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = self.queryset.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

        print(user.username)
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response({"detail": "Пароль успешно изменен."}, status=status.HTTP_200_OK)
    
    
class TableColumnNamesViewSet(ListModelMixin, GenericViewSet):
    queryset = TableColumnName.objects.all()
    serializer_class = GetTableColumnNamesSerializer
    
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(operation_summary="Передает названия колонок",
                         operation_description="Возвращает словарь, где ключ - название переменной из модели \
                             значение - название колонки, в которой будут отображаться данные из этой переменной.",
                         tags=["Table names"])
    def list(self, request, *args, **kwargs):
        fill_columns_names.fill_fact_table_names()
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = Response(serializer.data)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok
        return response
        
        
def export_fact_excel(request):
    workbook = xlsxwriter.Workbook('fact.xlsx')
    worksheet = workbook.add_worksheet()
    export_functions.create_fact_excel_table(workbook, worksheet)
    worksheet.title = 'Fact Table'

    workbook.close()

    response = FileResponse(open('fact.xlsx', 'rb'))
    response['ngrok-skip-browser-warning'] = 'skip-browser-warning'  #нужен исключительно для хоста через ngrok

    return FileResponse(open('fact.xlsx', 'rb'))


def export_plan_excel(request):
    workbook = xlsxwriter.Workbook('plan.xlsx')
    worksheet = workbook.add_worksheet()
    export_functions.create_plan_excel_table(workbook, worksheet)
    worksheet.title = 'Plan Table'

    workbook.close()

    return FileResponse(open('plan.xlsx', 'rb'))


def export_fact_plan_excel(request):
    workbook = xlsxwriter.Workbook('fact_plan.xlsx')
    worksheet = workbook.add_worksheet()
    export_functions.create_fact_plan_excel_table(workbook, worksheet)
    worksheet.title = 'Fact Plan Table'

    workbook.close()

    return FileResponse(open('fact_plan.xlsx', 'rb'))


def export_report_docx(request):
    doc = DocxTemplate('шаблон.docx')
    context = export_functions.get_context_dictionary()
    print(context)
    doc.render(context)
    doc.save('Report.docx')

    return FileResponse(open('Report.docx', 'rb'))


def export_report_pdf(request):
    doc = DocxTemplate('шаблон.docx')
    context = export_functions.get_context_dictionary()
    print(context)
    doc.render(context)
    doc.save('Report.docx')

    document = Document()
    # Load a Doc or Docx file
    document.LoadFromFile('Report.docx')

    # Create a ToPdfParameterList object
    parameter = ToPdfParameterList()

    # Disable hyperlinks in generated document
    parameter.DisableLink = True

    # Embed fonts in generated document
    parameter.IsEmbeddedAllFonts = True

    # Save the Word document to PDF
    document.SaveToFile("Report.pdf", parameter)
    document.Close()

    return FileResponse(open('Report.pdf', 'rb'))


def fact_data_view(request):
    # URL вашего API
    api_url = 'http://localhost:8000/data/fact/'

    # Отправляем GET-запрос к API
    response = requests.get(api_url)
    print(response.status_code)

    if response.status_code == 200:
        fact_data = response.json()
        return render(request, 'calculatorFactPlan/fact_data.html', {'fact_data': fact_data})
    else:
        return render(request, 'calculatorFactPlan/error.html', {'error': 'Ошибка при получении данных'})
