# Generated by Django 4.1.7 on 2023-04-28 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0014_alter_sono_acordou_alter_sono_dormiu'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='description',
            field=models.CharField(default=1, max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='link',
            field=models.TextField(default=1, max_length=3000),
            preserve_default=False,
        ),
    ]
