from django.db import models


class TipoUsuario(models.Model):

    nombre = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)