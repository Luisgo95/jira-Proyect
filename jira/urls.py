from django.urls import path, include 


from rest_framework.routers import DefaultRouter


from jira.views import  v_tipos_usuarios,v_estados_tarea , v_tarea


router = DefaultRouter()
# router.register(r'cursos',v_cursos.CursosViewSet, basename='cursos')
# router.register(r'unidades',v_unidades.UnidadesViewSet, basename='unidades')
router.register(r'tipo-usuarios',v_tipos_usuarios.TipoUsuarioViewSet, basename='tipo-usuarios')
router.register(r'estados-tarea',v_estados_tarea.EstadosTareaViewSet, basename='estados-tarea')
router.register(r'tareas',v_tarea.TareaViewSet, basename='tareas')
app_name = "app"
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('',include(router.urls))
    ]