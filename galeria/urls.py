from django.urls import path
from galeria.views import index, treinos, sono

urlpatterns = [
    path('', index, name='index'),
    path('treinos', treinos, name='treinos'),
    path('sono', sono, name='sono'),
]