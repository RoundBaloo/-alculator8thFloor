from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import FactDataSerializer, PlanDataSerializer, InputedFieldsDataSerializer, UserSerializer, ChangePasswordSerializer, GetTableColumnNamesSerializer
from .models import Data, TableColumnName
from drf_yasg.utils import swagger_auto_schema
from .components.data_updater import DataUpdater
from rest_framework.permissions import IsAuthenticated
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


# таблица факта
class FactDataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = FactDataSerializer

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get all calculated data",
                         operation_description="Returns a list of all calculated data entries")
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = Response(serializer.data)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'
        return response


class PlanDataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = PlanDataSerializer

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get all calculated data",
                         operation_description="Returns a list of all calculated data entries")
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = Response(serializer.data)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'
        return response


class InputedDataViewSet (viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = InputedFieldsDataSerializer

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get data that user can input",
                         operation_description="Returns a list of input data")
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = Response(serializer.data)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'
        return response

    def create(self, request, *args, **kwargs):
        # Получаем данные из запроса
        data = json.loads(request.GET.get('data'))
        print(data['cnt_UZ'])
        table = request.GET.get('table')
        data_updater = DataUpdater(data)
        data_updater.update_inputed_data(table)

        response = Response({"message": "All Data objects have been updated"}, status=status.HTTP_200_OK)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'

        return response


class HeadViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response = Response(serializer.data)
        response['ngrok-skip-browser-warning'] = 'skip-browser-warning'

        return response

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Проверка на наличие обязательных полей
        if not email or not password or not username:
            response = Response({"error": "required fields are not filled in"}, status=status.HTTP_400_BAD_REQUEST)
            response['ngrok-skip-browser-warning'] = 'skip-browser-warning'
            return response
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            response = Response({"message": "User  created successfully.", "user_id": user.id}, status=status.HTTP_201_CREATED)
            response['ngrok-skip-browser-warning'] = 'skip-browser-warning'
            print('success')
            return response
        except Exception as e:
            print('error')
            response = Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            response['ngrok-skip-browser-warning'] = 'skip-browser-warning'
            return response

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"error": "У вас нет прав на удаление пользователей"}, status=status.HTTP_403_FORBIDDEN)

        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Пользователь успешно удален"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, partial=False):
        try:
            user = self.queryset.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

        print(user.username)
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response({"detail": "Пароль успешно изменен."}, status=status.HTTP_200_OK)
    
    
class TableColumnNamesViewSet(viewsets.ModelViewSet):
    queryset = TableColumnName.objects.all()
    serializer_class = GetTableColumnNamesSerializer
    
    def list(self, request, *args, **kwargs):
        fill_columns_names.fill_fact_table_names()
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
        


def export_fact_excel(request):
    workbook = xlsxwriter.Workbook('fact.xlsx')
    worksheet = workbook.add_worksheet()
    export_functions.create_fact_excel_table(workbook, worksheet)
    worksheet.title = 'Fact Table'

    workbook.close()

    response = FileResponse(open('fact.xlsx', 'rb'))
    response['ngrok-skip-browser-warning'] = 'skip-browser-warning'

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
