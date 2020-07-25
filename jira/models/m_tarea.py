from django.db import models
from jira.models.m_estados_tarea import EstadosTarea
from jira.models.m_users import Account

class Tarea(models.Model):

    nombre = models.CharField(max_length=15)
    descripcion =  models.CharField(max_length=256)
    responsable = models.ForeignKey('Account', on_delete=models.CASCADE,related_name='responsable')
    informador = models.ForeignKey('Account', on_delete=models.CASCADE,related_name='informador')
    estado = models.CharField(max_length=256, default="Por Hacer")

    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)