from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Produto(models.Model):
    guardado = (
        ("aberto", "aberto"),
        ("estoque", "estoque")
    )
    quantidade = (
        ("Acabando", "Acambando"), ("Acabou", "Acabou"), ("Cheio", "Cheio")
    )
    nome = models.CharField(max_length=200)
    numero = models.IntegerField()
    local = models.CharField(max_length=200)
    descricao = models.TextField()
    validade = models.DateField()
    marca = models.CharField(max_length=200)
    armazenamento = models.CharField(
        max_length=10, choices=guardado, blank=False, null=False)
    situacao = models.CharField(
        max_length=20, choices=quantidade, blank=False, null=False)

    def __str__(self):
        return self.nome