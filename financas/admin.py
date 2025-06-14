from django.contrib import admin
from .models import Despesa, Receita, Venda # <--- Certifique-se que Venda está aqui

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'categoria', 'data', 'paga')
    list_filter = ('categoria', 'paga', 'data')
    search_fields = ('descricao', 'observacoes')
    date_hierarchy = 'data'
    list_editable = ('paga',)

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'origem', 'data')
    list_filter = ('origem', 'data')
    search_fields = ('descricao', 'observacoes')
    date_hierarchy = 'data'

@admin.register(Venda) # <--- Adicione este bloco para registrar Venda
class VendaAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'pelucia', 'quantidade', 'valor_venda', 'total_venda', 'data_venda', 'forma_pagamento')
    list_filter = ('maquina', 'pelucia', 'forma_pagamento', 'data_venda')
    search_fields = ('maquina__identificacao', 'pelucia__nome', 'forma_pagamento')
    date_hierarchy = 'data_venda'
    readonly_fields = ('total_venda',)