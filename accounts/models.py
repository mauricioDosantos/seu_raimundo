from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager, BaseUserManager
from django.db import models

# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
class UserCustomManager(BaseUserManager):
	def create_user(self, email, password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email)
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None):
            user = self.create_user(
                email,
                password=password,
            )
            user.is_admin = True
            user.save(using=self._db)
            return user


class UserCustom(AbstractBaseUser):
    email = models.EmailField(primary_key=True, unique=True)
    username = models.CharField(max_length=250, blank=True, null=True)
    contato = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # retornado get_email_field_name()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    #REQUIRED_FIELDS = ['email']
    objects = UserCustomManager()

    def __str__(self):
        status = 'Desativado'
        if self.active:
            status = 'Ativo'

        return f"{self.email} - {status}"
