from django.urls import path
from galeria.views import index, treinos, sono, treino_selecionado, pesos

urlpatterns = [
    path('', index, name='index'),
    path('treinos', treinos, name='treinos'),
    path('sono', sono, name='sono'),
    path('treino_selecionado/<int:treino_id>', treino_selecionado, name='treino_selecionado'),
    path("pesos",pesos, name='pesos'),
]