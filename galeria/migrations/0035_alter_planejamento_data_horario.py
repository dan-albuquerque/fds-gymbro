# Generated by Django 4.1.7 on 2023-05-24 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0034_merge_20230524_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 16, 46, 24, 987538)),
        ),
    ]
