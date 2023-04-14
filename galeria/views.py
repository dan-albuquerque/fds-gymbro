from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from galeria.models import Treinos, Exercise
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'galeria/index.html')

def treinos(request):
    treinos = Treinos.objects.all()

    return render(request, 'galeria/treinos.html', {'cards': treinos})

def treinos2(request):
    return render(request, 'galeria/treinos2.html')

def sono(request):
    return render(request, 'galeria/sono.html')

def sono2(request):
    return render(request, 'galeria/sono2.html')

def treino_selecionado(request, treino_id):
    treino_escolhido = get_object_or_404(Treinos, pk=treino_id) 

    return render(request, 'galeria/treino_selecionado.html', {"treino": treino_escolhido})

def pesos(request):
    return render(request, 'galeria/pesos.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Faça login automaticamente após o cadastro
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'galeria/register.html', {'form': form})

def treino_selecionado2(request, option):
    if option == 'peitoral':
        exercises = Exercise.objects.filter(group='peitoral')
    elif option == 'costas':
        exercises = Exercise.objects.filter(group='costas')
    elif option == 'perna':
        exercises = Exercise.objects.filter(group='perna')
    else:
        exercises = None
    if request.method == 'POST':
        for exercise in exercises:
            weight = request.POST.get('peso_ex{}')
            if weight is not None and weight != '':
                exercise.weight = weight
                exercise.save()

            #exercise.weight = Exercise(weight=weight)
    #exercise.weight.save()

    context = {
        'option': option.capitalize(),
        'exercises': exercises,
    }

    return render(request, 'galeria/treino_selecionado2.html', context)
def home(request):
    return render(request, 'galeria/home.html')
