# Generated by Django 4.2.3 on 2023-07-18 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 13, 51, 22, 470710)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 13, 51, 22, 470710)),
        ),
    ]