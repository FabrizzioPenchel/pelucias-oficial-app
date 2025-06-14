from django.shortcuts import render
from .models import Pelucia # Importa o modelo Pelucia

def lista_pelucias(request):
    # Busca todas as pelúcias ativas ordenadas por nome
    pelucias = Pelucia.objects.filter(ativa=True).order_by('nome')
    # Cria um dicionário para passar os dados para o template
    context = {
        'pelucias': pelucias,
        'titulo_pagina': 'Nossas Pelúcias'
    }
    # Renderiza o template 'pelucias/lista_pelucias.html' passando os dados
    return render(request, 'pelucias/lista_pelucias.html', context)