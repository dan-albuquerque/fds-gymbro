# Generated by Django 4.1.7 on 2023-05-09 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0019_delete_horarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 9, 55, 37, 295962)),
        ),
        migrations.AddField(
            model_name='planejamento',
            name='dia_semana',
            field=models.CharField(default='segunda', max_length=40),
        ),
    ]
