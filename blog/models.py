from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=30)

    descricao_1 = models.TextField(max_length=600)
    descricao_2 = models.TextField(max_length=600)
    descricao_3 = models.TextField(max_length=600)
    descricao_4 = models.TextField(max_length=600)
    descricao_5 = models.TextField(max_length=600)
    descricao_6 = models.TextField(max_length=600)
    descricao_7 = models.TextField(max_length=600)
    imagem = models.ImageField(blank = True)

    def __str__(self):
        return self.nome