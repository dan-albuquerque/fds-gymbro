# Generated by Django 4.1.7 on 2023-06-09 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0049_alter_planejamento_data_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejamento',
            name='treinoFeito',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 16, 7, 43, 666609)),
        ),
    ]
