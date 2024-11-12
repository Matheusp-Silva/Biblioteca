from django.db import models

class Usuario(models.Model):

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=64) # Cha 256 hash

    def __str__(self):
        return self.nome