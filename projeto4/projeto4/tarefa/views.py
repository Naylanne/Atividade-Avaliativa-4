from rest_framework import viewsets 
from .models import Tarefa
from .serializers import TarefaSerializer
from django_filters.rest_framework import DjangoFilterBackend 

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all() 
    serializer_class = TarefaSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'status', 'prioridade', 'data_limite', 'projeto']