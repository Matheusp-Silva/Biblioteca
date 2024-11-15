from django.db import models
from datetime import datetime
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome




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
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome