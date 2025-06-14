from django.db import models

class Pelucia(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Pelúcia")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Custo")
    estoque_total = models.IntegerField(default=0, verbose_name="Estoque Total")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    ativa = models.BooleanField(default=True, verbose_name="Ativa")

    class Meta:
        verbose_name = "Pelúcia"
        verbose_name_plural = "Pelúcias"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_estoque_disponivel(self):
        return self.estoque_total