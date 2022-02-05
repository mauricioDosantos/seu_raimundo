from django.apps import AppConfig
from django.db.models.signals import pre_save


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    #def ready(self):
    #    from .models import SuperUserCustom
    #    user_model  = self.get_model('SuperUserCustom')

    #    pre_save.connect(receiver, sender='account.SuperUserCustom')
