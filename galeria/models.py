from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from datetime import datetime   
from django.contrib.auth import get_user_model

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
    dormiu = models.TimeField(default=None)
    acordou = models.TimeField(default=None)
    total_sono = models.IntegerField(null=True, blank=True)
 
    def calcular_horas(self):
        dormiu = self.dormiu.hour + self.dormiu.minute / 60
        acordou = self.acordou.hour + self.acordou.minute / 60
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
    
    def save(self, *args, **kwargs):
        if not self.user_id:  # Verifica se o usuário já está definido
            User = get_user_model()
            self.user = User.objects.get(pk=User.id)
        super().save(*args, **kwargs)
        
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
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    treinoFeito = models.BooleanField(default=False)
    data_horario = models.DateTimeField(default=datetime.now(), blank=False) #armazena hj
    dia_semana = models.CharField(default='segunda', max_length=40)

class Historico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quantidade_treinos = models.IntegerField(default=0)


    def increment_quantidade_treinos(self):
        self.quantidade_treinos += 1
        self.save()


class Customizar(models.Model):
    nome = models.CharField(max_length=100)
    series = models.IntegerField()
    repeticoes = models.IntegerField()
    descanso = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    treino = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

