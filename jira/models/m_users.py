from django.db import models
from jira.models.m_tipo_usuario import TipoUsuario
from django.contrib.auth.models import AbstractUser

# class MyUserManager(BaseUserManager):
#     def create_user(self,email,username,password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Usernames must")
#         user = self.model(
#             email= self.normalize_email(email),
#             username= username
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
    
#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email= self.normalize_email(email),
#             password=password,
#             username= username
#         )
#         user.save(using=self._db)
#         return user

    
class Account(AbstractUser):

    email=models.EmailField(verbose_name='email', max_length=60, unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    tipo = models.ForeignKey('TipoUsuario', on_delete=models.CASCADE)

    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username','first_name','last_name']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username