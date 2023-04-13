from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Treinos
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'galeria/index.html')

def treinos(request):
    treinos = Treinos.objects.all()

    return render(request, 'galeria/treinos.html', {'cards': treinos})

def sono(request):
    return render(request, 'galeria/sono.html')

def treino_selecionado(request, treino_id):
    treino_escolhido = get_object_or_404(Treinos, pk=treino_id) 

    return render(request, 'galeria/treino_selecionado.html', {"treino": treino_escolhido})

def pesos(request):
    return render(request, 'galeria/pesos.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('')
    else:
        form = RegisterForm()

    return render(response, "galeria/register.html", {"form":form})