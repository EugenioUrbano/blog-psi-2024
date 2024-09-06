from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=30)
    descricao_1 = models.TextField()
    descricao_2 = models.TextField()
    descricao_3 = models.TextField()
    descricao_4 = models.TextField()
    descricao_5 = models.TextField()
    descricao_6 = models.TextField()
    descricao_7 = models.TextField()

    def __str__(self):
        return self.nome