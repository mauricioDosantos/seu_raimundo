from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import models


# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
class UserCustomManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserCustom(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=300, unique=True, verbose_name='Email'
    )
    contato = models.CharField(
        max_length=500, blank=True, null=True, verbose_name='Contato'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Ativo?'
    )
    is_admin = models.BooleanField(
        default=False, verbose_name='Administrador?'
    )

    objects = UserCustomManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        status = 'Desativado'
        if self.is_active:
            status = 'Ativo'

        return f"{self.email} - {status}"

    @property
    def is_staff(self):
        return self.is_admin
