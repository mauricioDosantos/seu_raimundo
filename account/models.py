from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.validators import validate_email
from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


# limite de tentativas, não protege de brute force
# retornar um PermissionDenied -> django não consulta outros backends
# dados de sessão guardam o backend onde foi autenticado
# references
# https://docs.djangoproject.com/en/4.0/topics/auth/default/
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#extending-user
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#extending-user
# https://medium.com/@gabrielfgularte/custom-user-model-no-django-d9bdf2838bd8
# https://docs.djangoproject.com/en/4.0/topics/auth/passwords/


class SuperUserCustom(AbstractBaseUser):
    email = models.EmailField(primary_key=True, unique=True)
    contato = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)

    # retornado get_email_field_name()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        status = 'Desativado'
        if self.active:
            status = 'Ativo'

        return f"{self.email} - {status}"


'''
# backend auth
class AuthBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None):

        #pwd_valid = check_password(password, )
        if email and password:
            try:
                validate_email(email)
                user_auth = SuperUser.objects.get(email=email)

            except (User.DoesNotExist, ValidationError):
                return PermissionDenied

'''
