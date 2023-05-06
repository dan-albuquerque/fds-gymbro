from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from galeria.models import Treinos, Exercise, Sono, UserObjective, Planejamento
from .forms import RegisterForm, SonoForm, PlanejamentoForm
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
               return redirect('home')
       else:
           messages.error(request, 'Invalid username or password!')
   else:
       form = AuthenticationForm()
   return render(request, 'galeria/index.html', {'form': form})

@login_required
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
    user_objective, created = UserObjective.objects.get_or_create(user=request.user)

    print(user_objective.selected_objective)#não estou conseguindo visualizar

    if request.method == "POST":
        objetivo = request.POST.get("objetivo")
        if objetivo:
            user_objective.selected_objective = objetivo
            user_objective.save()
            
    exercises = Exercise.objects.filter(user=request.user)

    if user_objective.selected_objective == 'hipertrofia':
        # repetições dos exercícios passam a ser 12
        for exercise in exercises:
            exercise.reps = 12
            exercise.rest = '30s'
            exercise.save()

    elif user_objective.selected_objective == 'resistencia':
        # repetições dos exercícios passam a ser 15
        for exercise in exercises:
            exercise.reps = 15
            exercise.rest = '60s'
            exercise.save()

    else:
        # repetições dos exercícios passam a ser 10
        for exercise in exercises:
            exercise.reps = 8
            exercise.rest = '120s'
            exercise.save()

    return render(request, 'galeria/treinos.html', {'cards': treinos, 'user_objective': user_objective})

####
@login_required(login_url='/')
def sono(request):
   if request.method == 'POST':
       form = SonoForm(request.POST)
       if form.is_valid():
           sono = form.save(commit=False)
           sono.user = request.user
           sono.calcular_horas()
           sono.save()
           return redirect(request.path)
   else:
       form = SonoForm()

   latest_sono = Sono.objects.filter(user=request.user).last()

   context = {'form': form, 'sono': latest_sono}

   return render(request, 'galeria/sono.html', context)

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
    latest_sono = Sono.objects.filter(user=request.user).last()
    context = {'sono': latest_sono}
    return render(request, 'galeria/home.html', context)

@login_required(login_url='/')
def sono_selecionado(request, id_sono):
   sono = Sono.objects.get(id=id_sono)
   return render(request, 'galeria/sono_selecionado.html', {'sono': sono})

@login_required(login_url='/')
def planejamento(request):
    if request.method == 'POST':
        form = PlanejamentoForm(request.POST)
        if form.is_valid():
            planos = form.save(commit=False)
            planos.user = request.user
            planos.save()
            return redirect(request.path)
    else:
        form = PlanejamentoForm()

    horarios = Planejamento.objects.filter(user=request.user).last()
    return render(request, 'galeria/planejamento.html', {'form': form, 'planejamentos': horarios})