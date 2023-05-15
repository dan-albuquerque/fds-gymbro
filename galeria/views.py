from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from galeria.models import Treinos, Exercise, Sono, UserObjective, Planejamento
from .forms import RegisterForm, SonoForm, PlanejamentoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from datetime import date, timedelta

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
def execucao(request, exercise_id):
   exercise = Exercise.objects.get(id=exercise_id)
   context = {'exercise': exercise}
   return render(request, 'galeria/execucao.html', context)

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
            exercise.reps = 10
            exercise.rest = '60s'
            exercise.save()

    elif user_objective.selected_objective == 'resistencia':
        # repetições dos exercícios passam a ser 15
        for exercise in exercises:
            exercise.reps = 15
            exercise.rest = '30s'
            exercise.save()

    else:
        # repetições dos exercícios passam a ser 10
        for exercise in exercises:
            exercise.reps = 6
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
    # Exclui objetos antigos
    LIMITE_DIAS = 7
    data_limite = date.today() - timedelta(days=LIMITE_DIAS)
    Planejamento.objects.filter(user=request.user, data__lt=data_limite).delete()

    if request.method == 'POST':
        # Verifica se algum botão de "confirmar" foi clicado
        if 'confirmar_segunda1' in request.POST:
            horario = request.POST['segunda_horario1']
            dia_semana = "segunda-feira"
        elif 'confirmar_terca1' in request.POST:
            horario = request.POST['terca_horario1']
            dia_semana = "terca-feira"
        elif 'confirmar_quarta1' in request.POST:
            horario = request.POST['quarta_horario1']
            dia_semana = "quarta-feira"
        elif 'confirmar_quinta1' in request.POST:
            horario = request.POST['quinta_horario1']
            dia_semana = "quinta-feira" 
        elif 'confirmar_sexta1' in request.POST:
            horario = request.POST['sexta_horario1']
            dia_semana = "sexta-feira"
        elif 'confirmar_sabado1' in request.POST:
            horario = request.POST['sabado_horario1']
            dia_semana = "sabado"
        elif 'confirmar_domingo1' in request.POST:
            horario = request.POST['domingo_horario1']
            dia_semana = "domingo"
        Planejamento.objects.create(user=request.user, data=date.today(), horario=horario, dia_semana=dia_semana)

    form = PlanejamentoForm()
    planejamentos = Planejamento.objects.filter(user=request.user)
    context = {'form': form, 'planejamentos': planejamentos}
    return render(request, 'galeria/planejamento.html',context)