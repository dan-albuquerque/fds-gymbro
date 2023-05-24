from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from datetime import datetime   
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest = models.CharField(default='40s', max_length=30)
    weight = models.FloatField(default=1)
    description = models.CharField(max_length=3000)
    link = models.TextField(max_length=3000)

    def __str__(self):
        return self.name


class Sono(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dormiu = models.IntegerField(default= None)
    acordou = models.IntegerField(default= None)
    total_sono = models.IntegerField(null=True, blank=True)

    def calcular_horas(self):
        dormiu = int(self.dormiu)
        acordou = int(self.acordou)
        cont = 0

        while dormiu <= 23 and dormiu > acordou:
            if dormiu == 23:
                dormiu=0
                cont = cont+1
            cont=cont+1
            dormiu=dormiu+1
        while dormiu < acordou:
            cont = cont + 1
            dormiu = dormiu + 1

        self.total_sono = cont
        self.save()
        
class UserObjective(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    OBJETIVOS_CHOICES = [
        ("hipertrofia", "Hipertrofia"),
        ("resistencia", "Resistência"),
        ("forca", "Força"),
    ]
    selected_objective = models.CharField(max_length=100, choices=OBJETIVOS_CHOICES, default='hipertrofia')

class Planejamento(models.Model):
    TIPO_CHOICES = (
        ('perna', 'Perna'),
        ('costas', 'Costas'),
        ('peito', 'Peito'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    data_horario = models.DateTimeField(default=datetime.now(), blank=False) #armazena hj
    dia_semana = models.CharField(default='segunda', max_length=40)

    
