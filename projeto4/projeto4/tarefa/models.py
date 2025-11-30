from django.db import models
from projeto.models import Projeto

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ("baixa", "Baixa"),
        ("media", "Média"),
        ("alta", "Alta"),
    ]
    titulo = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES)
    data_limite = models.DateTimeField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
