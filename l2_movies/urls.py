"""Calculator level app URL config"""

from django.urls import path

from .views import MovieListView, MovieCreateView, DirectorCreateView, MovieDeleteView

app_name = "movies"

urlpatterns = [
    path("", MovieListView.as_view(), name="list"),
    path("nueva-pelicula/", MovieCreateView.as_view(), name="new_movie"),
    path("nuevo-director/", DirectorCreateView.as_view(), name="new_director"),
    path("eliminar-pelicula/<int:pk>", MovieDeleteView.as_view(), name="delete"),
]
