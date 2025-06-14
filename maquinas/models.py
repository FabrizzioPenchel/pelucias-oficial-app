from django.db import models
from pelucias.models import Pelucia # Importa o modelo Pelucia do app pelucias

class Maquina(models.Model):
    STATUS_CHOICES = [
        ('Operacional', 'Operacional'),
        ('Reparo', 'Em Reparo'),
        ('Manutencao', 'Em Manutenção'),
        ('Inativa', 'Inativa'),
    ]

    identificacao = models.CharField(max_length=50, unique=True, verbose_name="Identificação da Máquina")
    localizacao = models.CharField(max_length=200, verbose_name="Localização")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Operacional', verbose_name="Status")
    data_instalacao = models.DateField(auto_now_add=True, verbose_name="Data de Instalação")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    capacidade_pelucias = models.IntegerField(default=100, verbose_name="Capacidade de Pelúcias")

    class Meta:
        verbose_name = "Máquina"
        verbose_name_plural = "Máquinas"
        ordering = ['localizacao', 'identificacao']

    def __str__(self):
        return f"{self.identificacao} ({self.localizacao})"

class EstoqueMaquina(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, related_name='estoques')
    pelucia = models.ForeignKey(Pelucia, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade de Pelúcias")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    class Meta:
        verbose_name = "Estoque da Máquina"
        verbose_name_plural = "Estoques das Máquinas"
        unique_together = ('maquina', 'pelucia')

    def __str__(self):
        return f"{self.maquina.identificacao} - {self.pelucia.nome}: {self.quantidade} unidades"