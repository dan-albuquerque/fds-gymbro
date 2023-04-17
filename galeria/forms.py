from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from galeria.models import Sono
'''
class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['nome_exercicio']
'''
class SonoForm(forms.ModelForm):
    class Meta:
        model = Sono
        fields = ['dormiu', 'acordou']
class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]