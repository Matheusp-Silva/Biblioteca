from django.urls import path
from livro import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='Cadastrar'),
]