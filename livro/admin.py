from django.contrib import admin
from .models import Livros, Categoria
from usuarios.models import Usuario

admin.site.register(Categoria)
admin.site.register(Livros)


