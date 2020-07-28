from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status, filters, viewsets
from rest_framework.response import Response
from jira.serializers import s_users
from jira.serializers.s_users import UserSerializer ,UserLoginSerializer,ReadUserSerializer
from jira.models.m_users import Account
from jira.utils.permissions import IsAccountOwner ,permissionUpdate, permissionCreateUser
from jira.permissions.p_users import UserPermission
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated
)

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = "nombre"
    search_fields = "nombre"
   # ordering_fields = "created"

    # queryset = Account.objects.all()
    serializer_class = s_users.UserSerializer
    #permission_classes = (permissions.IsAuthenticated)

    def get_permissions(self):
        if self.action in ['login']:
            permissions =[AllowAny]
        if self.action in ['create']:
            permissions = [permissionCreateUser]
        if self.action in ['retrieve','list']: 
           permissions = [IsAuthenticated,UserPermission, IsAccountOwner]
        if self.action in ['update','partial_update']: 
            permissions = [ permissionUpdate]
        # else:
        #     permissions = [IsAuthenticated]
        return [p() for p in permissions]


    # def list(self, request):
        # if (request.user.tipo.id==1):
        #      queryset = Account.objects.all()
        # else:
        #     queryset = Account.objects.filter(
        #         username = request.user.username
        #     )
        # serializer = UserSerializer(queryset, many=True)
        # return Response(serializer.data)



    def list(self, request):
        if (request.user.tipo.id==1):
             queryset = Account.objects.all()
        else:
            queryset = Account.objects.filter(
                username = request.user.username
            )
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


    # def partial_update(self, request, pk=None):
    #     print("Hola desde partial")
    #     serializer = UserSerializer(request.user, data=request.data, partial=True)
    #     serializer.save()
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data)



    @action(detail=False, methods=['post'])
    #signup es la etiqueta de la url asi lo redirigue asia aca... 
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user,token = serializer.save()
        data = {
            'access_token': token,
            'user': ReadUserSerializer(user).data
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


