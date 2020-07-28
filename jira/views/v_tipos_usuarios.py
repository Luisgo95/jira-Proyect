from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status, filters, viewsets

from jira.serializers import s_tipo_usuario
from jira.models.m_tipo_usuario import TipoUsuario
from jira.utils.permissions import permissionAdmin


class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = "nombre"
    search_fields = "nombre"
   # ordering_fields = "created"

    queryset = TipoUsuario.objects.all()
    serializer_class = s_tipo_usuario.TipoUsuarioModelSerializer
    def get_permissions(self):
        if self.action in ['create','update','list','delete','partial_update']:
            permissions = [permissionAdmin]
        return [p() for p in permissions]
    # @action(detail=True, methods=['post'])    
