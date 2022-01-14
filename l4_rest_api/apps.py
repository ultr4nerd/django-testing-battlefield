"""REST API level app"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class L4RestApiConfig(AppConfig):
    """REST API level app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'l4_rest_api'
    verbose_name = _("Level 4: REST API")
