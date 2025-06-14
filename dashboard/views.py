from django.shortcuts import render
from django.db.models import Sum
from maquinas.models import Maquina, EstoqueMaquina
from financas.models import Despesa, Receita 

def dashboard_view(request):
    # 1. Dados para "Máquinas de Pelúcia"
    maquinas_info = []
    maquinas = Maquina.objects.all().order_by('localizacao', 'identificacao')

    for maquina in maquinas:
        total_pelucias_na_maquina = EstoqueMaquina.objects.filter(maquina=maquina).aggregate(Sum('quantidade'))['quantidade__sum'] or 0

        maquinas_info.append({
            'id': maquina.identificacao,
            'localizacao': maquina.localizacao,
            'pelucias': total_pelucias_na_maquina,
            'status': maquina.status,
        })

    # 2. Total de Pelúcias (card)
    total_pelucias_em_maquinas = EstoqueMaquina.objects.aggregate(Sum('quantidade'))['quantidade__sum'] or 0

    # 3. Totais dos cards
    total_maquinas = Maquina.objects.count()

    # Cálculo de Receita e Despesas
    total_receita = Receita.objects.aggregate(Sum('valor'))['valor__sum'] or 0.00 
    total_despesas = Despesa.objects.filter(paga=True).aggregate(Sum('valor'))['valor__sum'] or 0.00

    # Despesas recentes para a tabela do dashboard (as últimas 5)
    despesas_recentes = Despesa.objects.filter(paga=True).order_by('-data')[:5]


    context = {
        'total_pelucias_cadastradas': total_pelucias_em_maquinas,
        'total_maquinas': total_maquinas,
        'total_receita': total_receita, # 
        'total_despesas': total_despesas,
        'maquinas_info': maquinas_info,
        'despesas_recentes': despesas_recentes,
    }
    return render(request, 'dashboard/dashboard.html', context)