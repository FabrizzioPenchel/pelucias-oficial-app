from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth # <--- Adicione esta importação
from maquinas.models import Maquina, EstoqueMaquina
from financas.models import Despesa, Receita, Venda # <--- Certifique-se que Venda está aqui

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

    # 4. Dados para o Gráfico de Pelúcias Distribuídas (NOVO)
    # Agrupar vendas por mês
    vendas_por_mes = Venda.objects.annotate(
        month=TruncMonth('data_venda') # Extrai o mês da data da venda
    ).values('month').annotate(
        total_vendido=Sum('quantidade') # Soma a quantidade vendida por mês
    ).order_by('month')

    chart_labels = [] # Nomes dos meses (ex: Jan, Fev)
    chart_data = [] # Quantidade de pelúcias vendidas

    for venda in vendas_por_mes:
        # Formata o mês para exibir no gráfico
        chart_labels.append(venda['month'].strftime('%b/%Y')) # Ex: Jun/2025
        chart_data.append(venda['total_vendido'])

    context = {
        'total_pelucias_cadastradas': total_pelucias_em_maquinas,
        'total_maquinas': total_maquinas,
        'total_receita': total_receita,
        'total_despesas': total_despesas,
        'maquinas_info': maquinas_info,
        'despesas_recentes': despesas_recentes,
        'chart_labels': chart_labels, # <--- Adicionado para o gráfico
        'chart_data': chart_data,   # <--- Adicionado para o gráfico
    }
    return render(request, 'dashboard/dashboard.html', context)