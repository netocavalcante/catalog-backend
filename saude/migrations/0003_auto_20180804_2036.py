# Generated by Django 2.1 on 2018-08-04 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saude', '0002_remove_samu_z_coordinate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samu',
            name='x_coordinate',
            field=models.DecimalField(decimal_places=15, max_digits=15),
        ),
        migrations.AlterField(
            model_name='samu',
            name='y_coordinate',
            field=models.DecimalField(decimal_places=15, max_digits=15),
        ),
    ]
