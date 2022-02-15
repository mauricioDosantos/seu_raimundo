from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager, BaseUserManager
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import password_validation
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
            user.is_superuser = True
            user.save(using=self._db)
            return user


class UserCustom(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=250, blank=True, null=True)
    contato = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


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
    def __int__(self):
        return 1
    #def is_staf(self):
    #    return True
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

'''
class AuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        if email and password:
            try:
                user = None# UserCustom.objects.get(email=email)
                user = validate_password(password, user)
            except UserCustom.DoesNotExist:
                return
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user
        else:
            return

    #def get_user(self, email):
    #    try:
    #        return User.objects.get(pk=email)
    #    except User.DoesNotExist:
    #        return

'''
