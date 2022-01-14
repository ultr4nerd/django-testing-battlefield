"""Login Form level app"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class L5LoginFormConfig(AppConfig):
    """Login Form level app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'l5_login_form'
    verbose_name = _("Level 5: Login Form")
