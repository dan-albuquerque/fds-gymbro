# Generated by Django 4.1.7 on 2023-06-09 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0048_merge_20230609_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 15, 56, 3, 335822)),
        ),
    ]
