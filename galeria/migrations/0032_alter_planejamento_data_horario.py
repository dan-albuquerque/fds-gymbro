# Generated by Django 4.1.7 on 2023-05-23 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0031_alter_planejamento_data_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 16, 38, 32, 770088)),
        ),
    ]
