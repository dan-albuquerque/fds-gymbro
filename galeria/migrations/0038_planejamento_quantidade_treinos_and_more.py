# Generated by Django 4.1.7 on 2023-05-26 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0037_merge_20230526_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejamento',
            name='quantidade_treinos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='weight',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 26, 8, 44, 13, 295856)),
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
