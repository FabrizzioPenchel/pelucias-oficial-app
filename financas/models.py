from django.db import models
from maquinas.models import Maquina
from pelucias.models import Pelucia

class Despesa(models.Model):
    CATEGORIA_CHOICES = [
        ('Compra de Pelúcias', 'Compra de Pelúcias'),
        ('Reparo de Máquinas', 'Reparo de Máquinas'),
        ('Transporte', 'Transporte'),
        ('Manutencao Geral', 'Manutenção Geral'),
        ('Aluguel', 'Aluguel'),
        ('Outros', 'Outros'),
    ]

    descricao = models.CharField(max_length=255, verbose_name="Descrição da Despesa")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateField(verbose_name="Data da Despesa")
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='Outros', verbose_name="Categoria")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    paga = models.BooleanField(default=True, verbose_name="Paga")

    class Meta:
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"
        ordering = ['-data', 'categoria']

    def __str__(self):
        return f"{self.descricao} - R${self.valor:.2f} ({self.data})"


class Receita(models.Model):
    ORIGEM_CHOICES = [
        ('Maquina', 'Venda em Máquina'),
        ('Pix', 'Pix Direto'),
        ('Dinheiro', 'Dinheiro em Espécie'),
        ('Outros', 'Outros Ganhos'),
    ]

    descricao = models.CharField(max_length=255, verbose_name="Descrição da Receita")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data = models.DateField(verbose_name="Data da Receita")
    origem = models.CharField(max_length=50, choices=ORIGEM_CHOICES, default='Maquina', verbose_name="Origem")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ['-data']

    def __str__(self):
        return f"{self.descricao} - R${self.valor:.2f} ({self.data})"


class Venda(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Máquina")
    pelucia = models.ForeignKey(Pelucia, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Pelúcia Vendida")
    quantidade = models.IntegerField(default=1, verbose_name="Quantidade Vendida")
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da Venda Unitário")  # Preço que o cliente pagou
    data_venda = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora da Venda")
    forma_pagamento = models.CharField(max_length=50, blank=True, null=True, verbose_name="Forma de Pagamento")

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ['-data_venda']

    def __str__(self):
        return f"Venda de {self.quantidade} {self.pelucia.nome if self.pelucia else 'Pelúcia Desconhecida'} em {self.maquina.identificacao if self.maquina else 'Máquina Desconhecida'} - R${self.total_venda:.2f}"

    @property
    def total_venda(self):
        return self.quantidade * self.valor_venda
