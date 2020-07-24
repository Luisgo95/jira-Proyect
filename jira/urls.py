from django.urls import path, include 


from rest_framework.routers import DefaultRouter


from jira.views import  v_tipos_usuarios


router = DefaultRouter()
# router.register(r'cursos',v_cursos.CursosViewSet, basename='cursos')
# router.register(r'unidades',v_unidades.UnidadesViewSet, basename='unidades')
router.register(r'tipo-usuarios',v_tipos_usuarios.TipoUsuarioViewSet, basename='tipo-usuarios')
app_name = "app"
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('',include(router.urls))
    ]