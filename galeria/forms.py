from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

'''
class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['nome_exercicio']
'''

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]