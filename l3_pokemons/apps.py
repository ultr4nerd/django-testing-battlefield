"""Pokémons level app"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class L3PokemonsConfig(AppConfig):
    """Pokémons level app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'l3_pokemons'
    verbose_name = _("Level 3: Pokémons")
