# Generated by Django 5.1.2 on 2024-10-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_grievance_area_alter_user_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grievance',
            name='area',
        ),
        migrations.RemoveField(
            model_name='user',
            name='area',
        ),
        migrations.AddField(
            model_name='grievance',
            name='aid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='aid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]