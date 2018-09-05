# Generated by Django 2.0.7 on 2018-07-21 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Samu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('geomtry_type', models.CharField(max_length=100)),
                ('x_coordinate', models.DecimalField(decimal_places=40, max_digits=50)),
                ('y_coordinate', models.DecimalField(decimal_places=40, max_digits=50)),
                ('z_coordinate', models.DecimalField(decimal_places=40, max_digits=50)),
            ],
        ),
    ]