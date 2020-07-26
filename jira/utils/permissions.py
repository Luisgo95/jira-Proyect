"""permisos para usuarios"""

#Django REST framework
from rest_framework.permissions import BasePermission
from jira.models.m_tarea import Tarea

class IsAccountOwner(BasePermission):
    def has_object_permissions(self, request,view,obj):
        return request.user == obj

class permissionUpdate(BasePermission):
    def has_permission(self, request,view):
        if(request.user.tipo.id==1):
            respuesta= True
        else:
            respuesta= False
        return respuesta


class permissionCreateTarea(BasePermission):
    def has_permission(self, request,view):
        if(request.user.tipo.id==1):
            respuesta= True
        else:
            respuesta= False
        return respuesta

class permissionUpdateTareas(BasePermission):
    def has_object_permission(self, request,view,obj):
        try:
            Tarea.objects.get(
                id = obj.id,
                responsable=request.user.id
            )
            return  True
        except Tarea.DoesNotExist:
            return False
     

# class permissionViewTarea(BasePermission):
#     def has_object_permission(self, request,view,obj):
#     try:
#         if(request.user.tipo.id==1):
#             respuesta= True
#         else:
#             respuesta= False
#     except 
#         return respuesta
