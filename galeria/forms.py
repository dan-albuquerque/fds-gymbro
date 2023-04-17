from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from galeria.models import Sono, Exercise
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

    def create_exercises(self, user):
        #olhar DEPOIS questao de sets, reps, etc
        Exercise.objects.create(user=user, name='supino reto barra', group='peitoral', sets=3, reps=10, rest=40, weight=10)
        Exercise.objects.create(user=user, name='supino inclinado halter + crucifixo halter', group='peitoral', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='tríceps pulley corda', group='peitoral', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='tríceps máquina', group='peitoral', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='elevação frontal', group='peitoral', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='tríceps francês', group='peitoral', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='desenvolvimento arnold', group='peitoral', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='puxada fechada', group='costas', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='remada com apoio aberta + fechada', group='costas', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='pullover polia + remada curvada', group='costas', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='rosca direta halter + braquial halter', group='costas', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='rosca scoth máquina', group='costas', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='hack', group='perna', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='leg 45°', group='perna', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='extensora', group='perna', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='flexora', group='perna', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='cadeira abdutora', group='perna', sets=3, reps=12, rest=45, weight=15)
        Exercise.objects.create(user=user, name='elevação panturrilha', group='perna', sets=3, reps=12, rest=45, weight=15)



    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            self.create_exercises(user)
        return user