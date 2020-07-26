"""permisos para usuarios"""

#Django REST framework
from rest_framework.permissions import BasePermission

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