from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from galeria.models import Treinos, Exercise, Sono
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in successfully!')
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
    else:
        form = AuthenticationForm()
    return render(request, 'galeria/index.html', {'form': form})

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
            weight = request.POST.get('peso_ex_{}'.format(exercise.pk))
            if weight is not None and weight != '':
                exercise.weight = weight
                exercise.save()

    context = {
        'option': option.capitalize(),
        'exercises': exercises,
    }

    return render(request, 'galeria/treino_selecionado2.html', context)

def home(request):
    return render(request, 'galeria/home.html')



def sono_selecionado(request):
    sono = Sono.objects.get(pk=1)
    if request.method == 'POST':
        dormiu = request.POST.get('dormiu')
        acordou = request.POST.get('acordou')
        sono.dormiu = dormiu
        sono.acordou = acordou
        sono.calcular_horas()
        sono.save()
    return render(request, 'galeria/sono_selecionado.html', {'sono': sono})

