from django.urls import path, include
from galeria.views import home, index, treinos, sono,  register, treino_selecionado2, logout_view, planejamento,execucao,historico,remove_workout
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

admin.site.logout_template = 'admin/logout.html' 
admin.site.logout_view = LogoutView.as_view(next_page='/admin/login/')

urlpatterns = [
    path('execucao/<int:exercise_id>/', execucao, name='execucao'),
    path('home', home, name='home'),
    path('', index, name='index'),
    path('logout/', logout_view, name='logout'),
    path('treinos/', treinos, name='treinos'),
    path('sono/',sono, name='sono'),
    path('', include("django.contrib.auth.urls")),
    path('register', register, name='register' ),
    path('treino_selecionado2/<str:option>/', treino_selecionado2, name='treino_selecionado2'), 
    path('planejamento', planejamento, name='planejamento'),
    path('historico/',historico,name='historico'),
    path('remove_workout/<int:id>/', remove_workout, name='remove_workout'),    
    #oq eh isso?
    #path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
    #n faço ideia meu brother -carlos
]
