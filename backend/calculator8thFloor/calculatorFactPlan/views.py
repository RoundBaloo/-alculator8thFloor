from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import HomeEmptySerializer, DataSerializer, InputedFieldsDataSerializer
from .models import Data
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from .components.data_updater import DataUpdater
# Create your views here.


class HomeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  
    serializer_class = HomeEmptySerializer 

    def list(self, request):
        return Response({"message": "Welcome to my API!"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response({"detail": "This is a detail view"})
    
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    
    @swagger_auto_schema(operation_summary="Get all calculated data",
                         operation_description="Returns a list of all calculated data entries")
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class InputedDataViewSet (viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = InputedFieldsDataSerializer
    
    @swagger_auto_schema(operation_summary="Get data that user can input",
                         operation_description="Returns a list of input data")
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
    def create(self, request, *args, **kwargs):
        # Получаем данные из запроса
        data = request.data
        data_updater = DataUpdater(data)
        data_updater.update_inputed_data()
        
        return Response({"message": "All Data objects have been updated"}, status=status.HTTP_200_OK)