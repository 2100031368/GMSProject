# Generated by Django 5.1.2 on 2024-10-11 09:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(100000000000), django.core.validators.MaxValueValidator(999999999999)])),
                ('name', models.CharField(max_length=150)),
                ('mobile', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('area', models.CharField(max_length=150)),
                ('flag', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('access', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField()),
                ('name', models.CharField()),
                ('phno', models.IntegerField()),
                ('issue_type', models.CharField(choices=[('WATER', 'WATER'), ('SEWAGE', 'SEWAGE'), ('ELECTRICITY', 'ELECTRICITY'), ('STREETLIGHT', 'STREETLIGHT'), ('MUNICIPAL SERVICES', 'MUNICIPAL SERVICES'), ('PARKS-PUBLIC SPACES', 'PARKS-PUBLIC SPACES'), ('PUBLIC TRANSPORT', 'PUBLIC TRANSPORT'), ('GOVT.SCHEMAS', 'GOVT.SCHEMAS'), ('OTHERS', 'OTHERS')])),
                ('issue', models.CharField()),
                ('viewflag', models.IntegerField(default=0)),
                ('solvedflag', models.IntegerField(default=0)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.user')),
            ],
        ),
    ]
