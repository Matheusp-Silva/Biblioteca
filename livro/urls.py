from django.urls import path
from livro import views

urlpatterns = [
    path('home/', views.home, name='home'),
]