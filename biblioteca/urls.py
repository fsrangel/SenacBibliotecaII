from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
    path('personalizar/', views.personalizar, name='personalizar'),
    path('logout/', views.user_logout, name='logout'),
]
