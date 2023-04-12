from django.db import models

# Create your models here.

class Exercicio(models.Model):
    NAME_EXERCISE_CHOICES = [
        ("back", "Back"),
        ("cardio", "Cardio"),
        ("chest", "Chest"),
        ("lower_arms", "Lower Arms"),
        ("lower_legs", "Lower Legs"),
        ("neck", "Neck"),
        ("shoulders", "Shoulders"),
        ("upper_arms", "Upper Arms"),
        ("upper_legs", "Upper Legs"),
        ("waist", "Waist"),
    ]

    nome_exercicio = models.CharField(max_length=50, choices=NAME_EXERCISE_CHOICES)
    descricao = models.TextField()


    def __str__(self):
        return self.nome_exercicio
