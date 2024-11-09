from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


# Create your models here.

# Data calculated by formulas
class Data(models.Model):
    machine_type = models.CharField(max_length=30)
    machine_type1 = models.CharField(max_length=30)
    month_files = models.IntegerField()
    avg_fact_files_per_month = models.IntegerField()
    cnt_machines = models.IntegerField()
    max_files = models.IntegerField()
    load_fact = models.CharField(max_length=10)
    scarcity_fact = models.IntegerField()
    cnt_UZ = models.IntegerField()
    load_plan = models.CharField(max_length=10)
    scarcity_plan = models.IntegerField()
    
