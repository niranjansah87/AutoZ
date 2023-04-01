# Generated by Django 4.1.7 on 2023-02-28 14:11

import RMSapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=RMSapp.models.uploaded_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('car_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('num_of_seats', models.IntegerField()),
                ('cost_par_day', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('employee_name', models.CharField(max_length=100)),
                ('cell_no', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('date', models.DateTimeField()),
                ('to', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PrivateMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
