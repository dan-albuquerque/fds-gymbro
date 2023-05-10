# Generated by Django 4.1.7 on 2023-05-06 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0016_treinos_objetivo_userobjective'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treinos',
            name='objetivo',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='rest',
            field=models.CharField(default='40s', max_length=30),
        ),
        migrations.CreateModel(
            name='Planejamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]