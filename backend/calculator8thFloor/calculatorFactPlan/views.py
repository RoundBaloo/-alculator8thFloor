from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import FactDataSerializer, PlanDataSerializer, InputedFieldsDataSerializer, UserSerializer
from .models import Data
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from .components.data_updater import DataUpdater
from rest_framework.permissions import IsAuthenticated
import json
from django.http import HttpResponse
import xlsxwriter
# Create your views here.


class FactDataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = FactDataSerializer

    permission_classes = [IsAuthenticated]

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
            print(email, password)
            response = Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            response['ngrok-skip-browser-warning'] = 'skip-browser-warning'
            return response
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            response = Response({"message": "User  created successfully.", "user_id": user.id}, status=status.HTTP_201_CREATED)
            response['ngrok-skip-browser-warning'] = 'skip-browser-warning'
            return response
        except Exception as e:
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

    def update(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"error": "У вас нет прав на изменение пользователей"}, status=status.HTTP_403_FORBIDDEN)

        try:
            partial = request.method == 'PATCH'
            user = User.objects.get(username='123')
            password = request.data.get('password')

            print(password)
            user.set_password(str(password))
            user.save()

            serializer = self.get_serializer(user, data=request.data, partial=partial)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def fact_export(request):
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=fact.xlsx"

    if request.GET:
        col = 0
        row = 0
        workbook = xlsxwriter.Workbook('fact.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.merge_range('A1:G1', 'ФАКТ')
