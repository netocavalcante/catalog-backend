# Generated by Django 2.1 on 2018-09-04 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saude', '0015_auto_20180904_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadesaude',
            name='municipio',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
