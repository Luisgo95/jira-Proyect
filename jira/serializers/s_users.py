from rest_framework import serializers
from django.contrib.auth.models import User
from jira.serializers.s_tipo_usuario import TipoUsuarioModelSerializer
from jira.models.m_users import Account

class UserSerializer(serializers.ModelSerializer):

    #profile = ProfileSerializer(required=False)
    #tipo=TipoUsuarioModelSerializer()

    class Meta:
        model = Account
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'tipo'
        )