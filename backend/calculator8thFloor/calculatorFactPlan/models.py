from django.db import models


# Create your models here.

# Data calculated by formulas
class Data(models.Model):
    machine_type = models.CharField(max_length=30)
    month_files = models.IntegerField()
    avg_fact_files_per_month = models.IntegerField()
    avg_fact_files_with_new = models.IntegerField()
    cnt_machines = models.IntegerField()
    max_files = models.IntegerField()
    load_fact = models.CharField(max_length=10)
    scarcity_fact = models.IntegerField()
    cnt_UZ = models.IntegerField()
    load_plan = models.CharField(max_length=10)
    scarcity_plan = models.IntegerField()
