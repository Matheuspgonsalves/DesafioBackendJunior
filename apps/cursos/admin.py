from django.contrib import admin
from .models import Cursos

class CursosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'carga_horaria')

admin.site.register(Cursos, CursosAdmin)
