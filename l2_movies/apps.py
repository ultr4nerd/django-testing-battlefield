"""Movies level app"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class L2MoviesConfig(AppConfig):
    """Movies level app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'l2_movies'
    verbose_name = _("Level 2: Movies")
