# Generated by Django 4.2.3 on 2023-07-27 14:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0003_projects_likes_count_alter_catalog_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 27, 14, 9, 32, 366948)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 27, 14, 9, 32, 366948)),
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('sending_date', models.DateTimeField(default=datetime.datetime(2023, 7, 27, 14, 9, 32, 366948))),
                ('phone', models.CharField(max_length=15)),
                ('author', models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
