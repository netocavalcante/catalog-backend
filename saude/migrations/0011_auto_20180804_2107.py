# Generated by Django 2.1 on 2018-08-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saude', '0010_auto_20180804_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samu',
            name='x_coordinate',
            field=models.DecimalField(decimal_places=40, max_digits=50),
        ),
        migrations.AlterField(
            model_name='samu',
            name='y_coordinate',
            field=models.DecimalField(decimal_places=40, max_digits=50),
        ),
    ]
