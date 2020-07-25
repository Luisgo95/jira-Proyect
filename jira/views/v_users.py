from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status, filters, viewsets
from rest_framework.response import Response
from jira.serializers import s_users
from jira.serializers.s_users import UserSerializer ,UserLoginSerializer,ReadUserSerializer
from jira.models.m_users import Account



class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = "nombre"
    search_fields = "nombre"
   # ordering_fields = "created"

    queryset = Account.objects.all()
    serializer_class = s_users.UserSerializer

    @action(detail=False, methods=['post'])
    #signup es la etiqueta de la url asi lo redirigue asia aca... 
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user,token = serializer.save()
        print(serializer)
        print(user)
        data = {
            'user': UserSerializer(user).data,
            'tipo' :"as",
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)  


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        usuario = Account.objects.get(username=request.data["username"])
        usuario.set_password(request.data["password"])
        usuario.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
  