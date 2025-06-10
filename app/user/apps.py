from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserConfig(AppConfig):
    name = 'app.user'
    label = 'user'
    verbose_name = _('Authentication and Authorization')
