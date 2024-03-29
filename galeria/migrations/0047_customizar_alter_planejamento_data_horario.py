# Generated by Django 4.1.7 on 2023-06-09 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0046_alter_planejamento_data_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customizar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('series', models.IntegerField()),
                ('repeticoes', models.IntegerField()),
                ('descanso', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('treino', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='planejamento',
            name='data_horario',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 14, 31, 56, 287409)),
        ),
    ]
