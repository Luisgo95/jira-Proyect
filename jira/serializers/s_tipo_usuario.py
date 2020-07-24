from rest_framework import serializers

from jira.models.m_tipo_usuario import TipoUsuario

class TipoUsuarioModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoUsuario
        fields = '__all__'

# class CursosReadSerializer(serializers.ModelSerializer):
#   #  profile = ProfileSerializer(required=False)

#     class Meta:
#         model = Cursos
#         fields = '__all__'