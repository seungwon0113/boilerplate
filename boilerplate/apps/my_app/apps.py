from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MyAppConfig(AppConfig):
    name = 'boilerplate.apps.my_app'
    verbose_name = _('My App')

