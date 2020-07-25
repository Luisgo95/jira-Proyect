from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status, filters, viewsets

from jira.serializers import s_users
from jira.models.m_users import Account



class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = "nombre"
    search_fields = "nombre"
   # ordering_fields = "created"

    queryset = Account.objects.all()
    serializer_class = s_users.UserSerializer
