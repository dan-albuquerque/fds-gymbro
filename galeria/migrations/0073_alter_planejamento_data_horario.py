# Generated by Django 4.2 on 2023-06-12 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0072_alter_planejamento_data_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 12, 7, 19, 21, 217459)),
        ),
    ]
