from django.urls import path, include
from galeria.views import index, treinos, sono, treino_selecionado, pesos, register, treino_selecionado2, treinos2, sono2

urlpatterns = [
    path('', index, name='index'),
    path('treinos', treinos, name='treinos'),
    path('treinos2/', treinos2, name='treinos2'),
    path('sono', sono, name='sono'),
    path('treino_selecionado/<int:treino_id>', treino_selecionado, name='treino_selecionado'),
    path("pesos",pesos, name='pesos'),
    path('', include("django.contrib.auth.urls")),
    path('register', register, name='register' ),
    path('treino_selecionado2/<str:option>', treino_selecionado2, name='treino_selecionado2'),
    path('sono2',sono2, name='sono2'),
]