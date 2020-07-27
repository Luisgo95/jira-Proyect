from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status, filters, viewsets
from rest_framework.response import Response
from jira.serializers import s_tarea
from jira.serializers.s_tarea import TareaModelSerializer
from jira.models.m_tarea import Tarea
from django.db.models import Count
from django.db.models import Sum,Min,Max, Avg,Q

#Prueba RSPONSE JSON serial
from django.http import JsonResponse
import json

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
        if self.action in['list','ProgressById']:
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

    @action(detail=False, methods=['get'])    
    def ProgressById(self,request):
        print("HOLA desde By ID")
        # grupos = Count('estado', filter=Q(responsable=request.user.id))
        # state1 = Tarea.objects.annotate(
        #     cantidad =Count('estado'))

        
        # y =json.dumps(state1)
        # print(y)
        
        #state01 = Tarea.objects.all().annotate(Count('estado'))
        # state01 = Tarea.objects.values('estado').annotate(dcount=Count('estado'))

        #query1=Tarea.objects.filter(responsable=request.user.id)

        state0 = Tarea.objects.values('estado').annotate(
            Total=Count('estado')
            ).filter(responsable=request.user.id).order_by()

           #filter=Q(book__rating__lte=5)
        # state1 = Tarea.objects.filter(responsable=request.user.id,estado=1).count()
        # state2 = Tarea.objects.filter(responsable=request.user.id,estado=2).count()
        # state3 = Tarea.objects.filter(responsable=request.user.id,estado=3).count()
        # data={
        #     "PorHacer" : state0,
        #     "Haciendo": state2,
        #     "Hecho": state3

        # }
        # #serializer = TareaModelSerializer(queryset, many=True)
        return Response(state0)

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