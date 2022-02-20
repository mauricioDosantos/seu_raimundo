from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import password_validation
#from django.contrib.auth import get_user_model
from .models import UserCustom


class AuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        if email and password:
            try:
                user = UserCustom.objects.get(email=email)
                #user = password_validation(password, user)
            except UserCustom.DoesNotExist:
                return
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user
        else:
            return
        return

    #def get_user(self, email):
    #    try:
    #        return User.objects.get(pk=email)
    #    except User.DoesNotExist:
    #        return
