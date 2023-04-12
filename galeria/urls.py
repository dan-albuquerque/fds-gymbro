from django.urls import path
from galeria.views import index, treinos, sono, treino_selecionado

urlpatterns = [
    path('', index, name='index'),
    path('treinos', treinos, name='treinos'),
    path('sono', sono, name='sono'),
    path('treino_selecionado', treino_selecionado, name='treino_selecionado')
]