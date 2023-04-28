from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from galeria.models import Treinos, Exercise, Sono
from .forms import RegisterForm, SonoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

@login_required(login_url='/')
def execução(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    context = {'exercise': exercise}
    return render(request, 'galeria/execução.html', context)
@login_required(login_url='/')
def treinos(request):
    treinos = Treinos.objects.all()

    return render(request, 'galeria/treinos.html', {'cards': treinos})

@login_required(login_url='/')
def treinos2(request):
    return render(request, 'galeria/treinos2.html')

@login_required(login_url='/')
@login_required(login_url='/')
def sono(request):
    if request.method == 'POST':
        form = SonoForm(request.POST)
        if form.is_valid():
            sono = form.save(commit=False)
            sono.user = request.user  # Associando o usuário atualmente autenticado à instância de Sono
            sono.calcular_horas()
            sono.save()
            return redirect('sono_selecionado', id_sono=sono.id)
    else:
        form = SonoForm()

    latest_sono = Sono.objects.filter(user=request.user).last()

    context = {'form': form, 'sono': latest_sono}

    return render(request, 'galeria/sono.html', context)

@login_required(login_url='/')
def sono2(request):
    return render(request, 'galeria/sono2.html')

@login_required(login_url='/')
def treino_selecionado(request, treino_id):
    treino_escolhido = get_object_or_404(Treinos, pk=treino_id) 

    return render(request, 'galeria/treino_selecionado.html', {"treino": treino_escolhido})

@login_required(login_url='/')
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

@login_required(login_url='/')
def treino_selecionado2(request, option):
    if option == 'peitoral':
        exercises = Exercise.objects.filter(user=request.user, group='peitoral')
    elif option == 'costas':
        exercises = Exercise.objects.filter(user=request.user, group='costas')
    elif option == 'perna':
        exercises = Exercise.objects.filter(user=request.user, group='perna')
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

@login_required(login_url='/')
def home(request):
    return render(request, 'galeria/home.html')


@login_required(login_url='/')
def sono_selecionado(request, id_sono):
    sono = Sono.objects.get(id=id_sono)
    return render(request, 'galeria/sono_selecionado.html', {'sono': sono})

#@login_required(login_url='/') VER DEPOIS
def planejamento(request):
    return render(request, 'galeria/planejamento.html')