from rest_framework import serializers

from jira.models.m_estados_tarea import EstadosTarea

class EstadosTareaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstadosTarea
        fields = '__all__'

# class CursosReadSerializer(serializers.ModelSerializer):
#   #  profile = ProfileSerializer(required=False)

#     class Meta:
#         model = Cursos
#         fields = '__all__'