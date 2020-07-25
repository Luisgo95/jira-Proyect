from rest_framework import serializers
from django.contrib.auth.models import User
from jira.serializers.s_tipo_usuario import TipoUsuarioModelSerializer
from jira.models.m_users import Account
from django.contrib.auth import authenticate, password_validation

from rest_framework.authtoken.models import Token

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
class ReadUserSerializer(serializers.ModelSerializer):

    #profile = ProfileSerializer(required=False)
    #tipo=TipoUsuarioModelSerializer()

    class Meta:
        model = Account
        fields = (
            'username',
            'email',
            'tipo',

            )

class UserLoginSerializer(serializers.Serializer):
     """"User login serializer
     Handel the login reques data"""
     email = serializers.EmailField()
     password = serializers.CharField(min_length=2, max_length=64)

     def validate(self,data):
         user = authenticate(email=data['email'], password=data['password'])

         if not user:
            
             raise serializers.ValidationError('Holis Invalid credentials')
        # if not user.is_verified:
        #     raise serializers.ValidationError('Account is not active yet :( ')
         self.context['user'] = user
        
         return data

     def create(self,data):
        token, created = Token.objects.get_or_create(user = self.context['user'])
        return self.context['user'], token.key
