from django.contrib import admin
from .models import Pelucia

@admin.register(Pelucia)
class PeluciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_custo', 'estoque_total', 'ativa', 'data_cadastro')
    search_fields = ('nome', 'descricao')
    list_filter = ('ativa', 'data_cadastro')
    list_editable = ('ativa',)