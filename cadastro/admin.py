from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','idade','email','contato')
    list_filter = ('nome',)
    list_fields = ('nome',)
    list_per_page = 10




    