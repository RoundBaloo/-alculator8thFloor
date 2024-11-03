from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from .serializers import GroupSerializer, UserSerializer, HomeEmptySerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HomeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  
    serializer_class = HomeEmptySerializer 

    def list(self, request):
        return Response({"message": "Welcome to my API!"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response({"detail": "This is a detail view"})