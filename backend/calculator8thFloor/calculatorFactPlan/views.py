from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import DataSerializer, InputedFieldsDataSerializer, UserSerializer
from .models import Data
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from .components.data_updater import DataUpdater
from rest_framework.permissions import IsAuthenticated
# Create your views here.

    
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    
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
    
    # permission_classes = [IsAuthenticated]
    
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
        data = request.data
        data_updater = DataUpdater(data)
        data_updater.update_inputed_data()
        
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
        username = request.data.get('email')
        email = request.data.get('email')
        password = request.data.get('password')

        # Проверка на наличие обязательных полей
        if not email or not password:
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