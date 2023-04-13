from django.db import models

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



class Exercicio(models.Model):
    NOME_EXERCICIOS_COSTAS = [
        ("puxada aberta", "Puxada aberta"),
        ("remada aberta", "Remada aberta"),
        ("pull over polia", "Pull over polia"),
        ("rosca halter", "Rosca halter"),
        ("rosca martelo halter", "Rosca martelo halter"),
        ("bíceps scoth", "Bíceps scoth")
    ]
    NOME_EXERCICIOS_PEITO = [
        ('Supino reto', 'supino reto'),   
        ('Desenvolvimento de Ombros', 'desenvolvimento de Ombros'),
        ('Tríceps Pulley', 'tríceps Pulley'),
        ('Tríceps testa', 'tríceps testa'),
        ('Supino inclinado', 'supino inlcinado'),   
    ]
    

    exercicio_costas = models.CharField(max_length=50, choices=NOME_EXERCICIOS_COSTAS)
    exercicio_peito = models.CharField(max_length=50, choices=NOME_EXERCICIOS_PEITO)
    tipo_treino = models.ForeignKey(Treinos, on_delete=models.CASCADE)
    numero_series = models.IntegerField()
    repeticoes = models.IntegerField()
    tempo_descanso = models.DurationField()