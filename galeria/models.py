from django.db import models
from django.contrib.auth.models import AbstractUser, User

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
    grupo = models.CharField(max_length=100, null=False, blank=False, default='')

class Exercise(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest = models.IntegerField(default=40)
    weight = models.IntegerField(default=1)

    def str(self):
        return self.name
    
class Sono(models.Model):
    dormiu = models.IntegerField(default=2)
    acordou = models.IntegerField(default=2)
    total_sono = models.IntegerField(null= True, blank=True)

    def calcular_horas(self):
        dormiu = int(self.dormiu)
        acordou = int(self.acordou)
        cont = 0

        while dormiu <= 24 and dormiu > acordou:
            cont = cont + 1
            dormiu = dormiu + 1
            if dormiu == 24:
                dormiu = 1
        while dormiu < acordou:
            cont = cont + 1
            dormiu = dormiu + 1
        
        self.total_sono = cont
        self.save()