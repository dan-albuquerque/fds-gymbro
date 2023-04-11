from django import forms
from .models import Exercicio

class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['nome_exercicio']