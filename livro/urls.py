from django.urls import path
from livro import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ver_livro/<int:id>', views.ver_livro, name='ver_livro')
]
