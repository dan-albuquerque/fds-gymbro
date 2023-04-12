from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExercicioForm

# Create your views here.
def index(request):
    return render(request, 'galeria/index.html')

def treinos(request):
    if request.method == 'POST':
        form = ExercicioForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para a página de sucesso
    else:
        form = ExercicioForm()

    return render(request, 'galeria/treinos.html', {'form': form})

def sono(request):
    return render(request, 'galeria/sono.html')

def treino_selecionado(request):
    return render(request, 'galeria/treino_selecionado.html')
def pesos(request):
    return render(request, 'galeria/pesos.html')