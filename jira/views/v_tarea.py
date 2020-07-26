from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status, filters, viewsets
from rest_framework.response import Response
from jira.serializers import s_tarea
from jira.serializers.s_tarea import TareaModelSerializer
from jira.models.m_tarea import Tarea

from jira.utils.permissions import permissionCreateTarea , permissionUpdateTareas
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated
)

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = "nombre"
    search_fields = "nombre"
   # ordering_fields = "created"

    queryset = Tarea.objects.all()
    serializer_class = s_tarea.TareaModelSerializer

    def get_permissions(self):
        if self.action in['list']:
            permissions =[IsAuthenticated]
        if self.action in ['create','retrieve']:
            permissions =[permissionCreateTarea]
        if self.action in ['partial_update']: 
            permissions = [permissionUpdateTareas]
        # else:
        #     permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def list(self, request):
        if (request.user.tipo.id==1):
             queryset = Tarea.objects.all()
        else:
            queryset = Tarea.objects.filter(
                responsable = request.user.id
            )
        serializer = TareaModelSerializer(queryset, many=True)
        return Response(serializer.data)


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