"""Calculator level app"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class L1CalculatorConfig(AppConfig):
    """Calculator level app config"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "l1_calculator"
    verbose_name = _("Level 1: Calculator")
