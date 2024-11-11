from django.contrib.auth.models import Group, User
from rest_framework import serializers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.utils import swagger_auto_schema
from .models import Data
        

class FactDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = [
            'machine_type',
            'month_files',
            'avg_fact_files_per_month',
            'cnt_machines',
            'max_files',
            'load_fact',
            'scarcity_fact'
        ]
        extra_kwargs = {
            'url': {'view_name': 'calculated-data-detail'},
        }
        

class PlanDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = [
            'machine_type',
            'month_files',
            'avg_fact_files_per_month',
            'avg_fact_files_with_new',
            'cnt_machines',
            'max_files',
            'load_plan',
            'scarcity_plan',
            'cnt_UZ'
        ]
        extra_kwargs = {
            'url': {'view_name': 'calculated-data-detail'},
        }


class InputedFieldsDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['machine_type', 'cnt_machines', 'avg_fact_files_per_month', 'cnt_UZ']
        extra_kwargs = {
            'url': {'view_name': 'input-data'},
        }
        
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'