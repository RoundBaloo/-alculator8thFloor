from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Data, TableColumnName
from rest_framework.exceptions import ValidationError


class FactDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = [
            'machine_type',
            'machine_name',
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
            'machine_name',
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
        fields = ['machine_type', 'cnt_machines', 'avg_fact_files_per_month', 'cnt_UZ', 'permitted_load']
        extra_kwargs = {
            'url': {'view_name': 'input-data'},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        # Проверка совпадения нового пароля
        if attrs['new_password'] != attrs['confirm_password']:
            raise ValidationError({"confirm_password": "Пароли не совпадают."})

        return attrs

    def save(self, user):
        user.set_password(self.validated_data['new_password'])
        user.save()
        

class GetTableColumnNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableColumnName
        fields = '__all__'