from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Treinos(models.Model):
    OPCOES_TREINOS = [
        ("peitoral", "Peitoral"),
        ("costas", "Costas"),
        ("perna", "Perna"),
    ]
    nome_treino = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    descricao = models.TextField(null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_TREINOS, default='')

class Exercise(models.Model):
    name = models.CharField(max_length=100) # exercise name
    group = models.CharField(max_length=50) # group ?= peitoral, costas ou perna
    sets = models.IntegerField() # sets number
    reps = models.IntegerField() # reps number
    #weight = models.IntegerField()
    
    def __str__(self):
        return self.name