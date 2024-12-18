from django.db import models
from datetime import datetime

# Вычисоленные данные
class Data(models.Model):
    machine_type = models.CharField(max_length=30)
    machine_name = models.CharField(max_length=30)
    month_files = models.IntegerField()
    avg_fact_files_per_month = models.IntegerField()
    avg_fact_files_with_new = models.IntegerField()
    new_users_files = models.IntegerField()
    cnt_machines = models.IntegerField()
    max_files = models.IntegerField()
    load_fact = models.CharField(max_length=10)
    scarcity_fact = models.IntegerField()
    cnt_UZ = models.IntegerField()
    load_plan = models.CharField(max_length=10)
    scarcity_plan = models.IntegerField()
    permitted_load = models.IntegerField()
    
    
    
# Названия для колонок
class TableColumnName(models.Model):
    month_files = models.CharField(max_length=40)
    avg_fact_files_per_month = models.CharField(max_length=40)
    avg_fact_files_with_new = models.CharField(max_length=40)
    new_users_files = models.CharField(max_length=40)
    cnt_machines = models.CharField(max_length=40)
    max_files = models.CharField(max_length=40)
    load_fact = models.CharField(max_length=40)
    scarcity_fact = models.CharField(max_length=40)
    cnt_UZ = models.CharField(max_length=40)
    load_plan = models.CharField(max_length=40)
    scarcity_plan = models.CharField(max_length=40)
    

class LastPasswordChangeDate(models.Model):
    username = models.CharField(max_length=40)
    last_password_change_date = models.DateField()
    