from django.db import models
from datetime import datetime

class Livros(models.Model):

    nome = models.CharField(max_length=50, null=False, blank=False)
    autor = models.CharField(max_length=30, null=False, blank=True)
    co_autor = models.CharField(max_length=30, blank=True, null=True)
    data_cadastro = models.DateTimeField(default=datetime.now, null=False, blank=False)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Livro'