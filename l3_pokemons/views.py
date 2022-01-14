"""Pokémons level app views"""

from django.views.generic import TemplateView

from .services import search_pokemon


class PokemonSearchView(TemplateView):
    """Search for a Pokémon by ID"""
    template_name = "l3_pokemons/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_id = self.request.GET.get("pokemon_id")
        if pokemon_id is not None:
            context["pokemon"] = search_pokemon(pokemon_id)
            print(context["pokemon"])
        return context
