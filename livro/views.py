from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros

def home(request):

    if request.session.get('usuario'):

        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)

        return render(request, 'home.html', {'usuario': usuario.nome, 'livros': livros})

    else:
        return redirect('/auth/login/')

def ver_livro(request, id):

    livro = Livros.objects.get(id=id)

    return render(request, 'ver_livro.html', {'livro': livro})