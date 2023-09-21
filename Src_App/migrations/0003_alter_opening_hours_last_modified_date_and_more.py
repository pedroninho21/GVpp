# Generated by Django 4.1.7 on 2023-09-07 04:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0002_used_car_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opening_hours',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 9, 37, 30, 756563), verbose_name='Last Modified'),
        ),
        migrations.AlterField(
            model_name='used_car',
            name='availability',
            field=models.BooleanField(default=True, verbose_name='Is Available'),
        ),
        migrations.AlterField(
            model_name='used_car',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 9, 37, 30, 755561), verbose_name='Last Edited on'),
        ),
    ]