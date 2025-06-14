from django.contrib import admin
from .models import Maquina, EstoqueMaquina # Ambas as classes devem ser importadas aqui

@admin.register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('identificacao', 'localizacao', 'status', 'data_instalacao', 'capacidade_pelucias')
    search_fields = ('identificacao', 'localizacao')
    list_filter = ('status', 'data_instalacao')
    list_editable = ('status',)

@admin.register(EstoqueMaquina)
class EstoqueMaquinaAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'pelucia', 'quantidade', 'data_atualizacao')
    list_filter = ('maquina', 'pelucia', 'data_atualizacao')
    search_fields = ('maquina__identificacao', 'pelucia__nome')
    raw_id_fields = ('maquina', 'pelucia')