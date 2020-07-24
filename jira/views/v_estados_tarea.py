from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status, filters, viewsets

from jira.serializers import s_estado_tarea
from jira.models.m_estados_tarea import EstadosTarea



class EstadosTareaViewSet(viewsets.ModelViewSet):
    queryset = EstadosTarea.objects.all()

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = "nombre"
    search_fields = "nombre"
   # ordering_fields = "created"

    queryset = EstadosTarea.objects.all()
    serializer_class = s_estado_tarea.EstadosTareaModelSerializer

    # @action(detail=True, methods=['post'])    
