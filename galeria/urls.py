from django.urls import path
from galeria.views import index, treinos

urlpatterns = [
    path('', index, name='index'),
    path('treinos', treinos, name='treinos'),
]