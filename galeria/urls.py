from django.urls import path, include
from galeria.views import home, index, treinos, sono, treino_selecionado, register, treino_selecionado2, treinos2, sono2, sono_selecionado, logout_view, planejamento,execução
from django.contrib import admin
from django.contrib.auth.views import LogoutView

admin.site.logout_template = 'admin/logout.html' 
admin.site.logout_view = LogoutView.as_view(next_page='/admin/login/')
urlpatterns = [
    path('execução/<int:exercise_id>/', execução, name='execução'),
    path('home', home, name='home'),
    path('', index, name='index'),
    path('logout/', logout_view, name='logout'),
    path('treinos', treinos, name='treinos'),
    path('treinos2/', treinos2, name='treinos2'),
    path('sono', sono, name='sono'),
    path('sono/', sono, name='sono'),
    path('treino_selecionado/<int:treino_id>', treino_selecionado, name='treino_selecionado'),
    path('', include("django.contrib.auth.urls")),
    path('register', register, name='register' ),
    path('sono2',sono2, name='sono2'),
    path('sono_selecionado/<int:id_sono>/',sono_selecionado, name='sono_selecionado'),
    path('treino_selecionado2/<str:option>/', treino_selecionado2, name='treino_selecionado2'), 
    path('planejamento', planejamento, name='planejamento'),

]