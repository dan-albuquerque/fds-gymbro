# Generated by Django 4.1.7 on 2023-06-08 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0043_alter_planejamento_data_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 22, 0, 21, 118844)),
        ),
    ]
