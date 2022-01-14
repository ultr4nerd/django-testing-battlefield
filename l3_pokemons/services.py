"""Pokémons level app services"""

from typing import Union

import requests


def search_pokemon(pokemon_id: Union[str, int]):
    """Search for a Pokémon"""
    if type(pokemon_id) == str and not pokemon_id.isdecimal():
        return None

    url = "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_id)
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
