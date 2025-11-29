from django.db import models
from projeto.models import Projeto

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    prioridade = models.PositiveIntegerField()
    data_limite = models.DateTimeField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo 