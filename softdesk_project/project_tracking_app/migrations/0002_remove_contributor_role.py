# Generated by Django 3.2.2 on 2021-06-07 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_tracking_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='role',
        ),
    ]
