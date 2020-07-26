from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status, filters, viewsets

from jira.serializers import s_tarea
from jira.models.m_tarea import Tarea



class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = "nombre"
    search_fields = "nombre"
   # ordering_fields = "created"

    queryset = Tarea.objects.all()
    serializer_class = s_tarea.TareaModelSerializer

    # @action(detail=True, methods=['post'])    
    # def perform_create(self,serializer):
    #     tarea = serializer.save()
    #     user = self.request.user
    #     Membership.objects.create(
    #         user=user,
    #         profile = profile,
    #         circle=circle,
    #         is_admin= True,
    #         remaining_invitations =10
    #     )