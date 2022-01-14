"""Testing Battlefield URL Configuration"""

from django.urls import path, include

from .views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("calculadora/", include("l1_calculator.urls")),
    path("peliculas/", include("l2_movies.urls")),
    path("pokemon/", include("l3_pokemons.urls")),
    path("api/", include("l4_rest_api.urls")),
    path("auth/", include("l5_login_form.urls")),
]
