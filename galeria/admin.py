from django.contrib import admin
from galeria.models import Treinos, Exercise, Sono

admin.site.register(Treinos)
admin.site.register(Exercise)
admin.site.register(Sono)

class ListandoTreinos(admin.ModelAdmin):
    list_display = ('id', 'nome_treino', 'legenda')
    list_display_links = ('id', 'nome')
    search_fields = ("nome",)
    list_filter = ('categoria',)

