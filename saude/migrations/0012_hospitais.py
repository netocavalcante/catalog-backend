# Generated by Django 2.1 on 2018-08-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saude', '0011_auto_20180804_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('endereco', models.CharField(max_length=400)),
                ('x_coordinate', models.DecimalField(decimal_places=40, max_digits=50)),
                ('y_coordinate', models.DecimalField(decimal_places=40, max_digits=50)),
            ],
        ),
    ]
