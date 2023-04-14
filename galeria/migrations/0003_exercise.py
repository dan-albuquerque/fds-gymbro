# Generated by Django 4.1.7 on 2023-04-14 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_delete_exercicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=50)),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
            ],
        ),
    ]
