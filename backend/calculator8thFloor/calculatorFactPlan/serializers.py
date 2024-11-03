from django.contrib.auth.models import Group, User
from rest_framework import serializers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="Get user details", responses={200: "User details"})
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


@swagger_auto_schema(operation_description="Get group details", responses={211: "Group details"})
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
        
@swagger_auto_schema(operation_description="Get group details", responses={200: "ABOBA"})
class HomeEmptySerializer(serializers.Serializer):
    pass