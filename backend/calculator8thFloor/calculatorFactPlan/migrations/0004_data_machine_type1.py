# Generated by Django 5.1.2 on 2024-11-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculatorFactPlan', '0003_data_delete_calculateddata'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='machine_type1',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
