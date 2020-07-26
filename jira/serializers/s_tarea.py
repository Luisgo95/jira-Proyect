from rest_framework import serializers

from jira.models.m_tarea import Tarea

class TareaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarea
        fields = (
            'id',
            'nombre',
            'descripcion',
            'responsable',
            'informador',
            'estado',
        )
