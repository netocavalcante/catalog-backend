# Generated by Django 2.0.7 on 2018-07-25 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saude', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samu',
            name='z_coordinate',
        ),
    ]
