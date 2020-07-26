
from rest_framework.permissions import BasePermission

#MODELS
from jira.models.m_users import Account

class UserPermission(BasePermission):
    def has_object_permissions(self, request, view, obj):
        try:
            1 == request.user.tipo.id
        except :
            return False
        return True