# Generated by Django 4.1.7 on 2023-05-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0020_planejamento_data_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejamento',
            name='dia_semana',
            field=models.CharField(default='segunda', max_length=40),
        ),
    ]
