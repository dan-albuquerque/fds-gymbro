# Generated by Django 4.1.7 on 2023-04-27 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0013_merge_20230426_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sono',
            name='acordou',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='sono',
            name='dormiu',
            field=models.IntegerField(default=None),
        ),
    ]
