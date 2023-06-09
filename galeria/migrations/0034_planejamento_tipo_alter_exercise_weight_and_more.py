# Generated by Django 4.1.7 on 2023-05-25 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0033_alter_planejamento_data_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejamento',
            name='tipo',
            field=models.CharField(choices=[('perna', 'Perna'), ('costas', 'Costas'), ('peito', 'Peito')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='weight',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 25, 8, 28, 46, 779123)),
        ),
    ]