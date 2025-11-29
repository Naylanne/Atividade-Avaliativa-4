from rest_framework import viewsets
from .models import Projeto
from .serializers import ProjetoSerializer
from django_filters.rest_framework import DjangoFilterBackend 

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all() 
    serializer_class = ProjetoSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'descricao', 'data_criacao']