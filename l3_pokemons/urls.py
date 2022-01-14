"""Pokémons level app URL config"""

from django.urls import path

from .views import PokemonSearchView

app_name = "pokemons"

urlpatterns = [
    path("", PokemonSearchView.as_view(), name="search"),
]
