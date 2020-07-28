from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status, filters, viewsets

from jira.serializers import s_estado_tarea
from jira.models.m_estados_tarea import EstadosTarea
from jira.utils.permissions import permissionAdmin


class EstadosTareaViewSet(viewsets.ModelViewSet):
    queryset = EstadosTarea.objects.all()

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = "nombre"
    search_fields = "nombre"
   # ordering_fields = "created"

    queryset = EstadosTarea.objects.all()
    serializer_class = s_estado_tarea.EstadosTareaModelSerializer
    def get_permissions(self):
        if self.action in ['create','update','list','delete','partial_update']:
            permissions = [permissionAdmin]
        return [p() for p in permissions]

    # @action(detail=True, methods=['post'])    
