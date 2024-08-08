from django.db import models
from django.contrib.auth import get_user_model

class Autor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ano_publicacao = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

