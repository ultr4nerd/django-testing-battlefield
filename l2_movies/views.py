"""Movies level app views"""

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .models import Movie, Director


class MovieListView(ListView):
    """Show all movies"""
    template_name = "l2_movies/list.html"
    queryset = Movie.objects.select_related("director").all()


class MovieCreateView(CreateView):
    """Create a new movie"""
    model = Movie
    fields = "__all__"
    template_name = "l2_movies/new_movie.html"
    success_url = reverse_lazy("movies:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["directors"] = Director.objects.all()
        return context


class DirectorCreateView(CreateView):
    """Create a new director"""
    model = Director
    fields = "__all__"
    template_name = "l2_movies/new_director.html"
    success_url = reverse_lazy("movies:list")


class MovieDeleteView(DeleteView):
    """Delete an existing movie"""
    model = Movie
    template_name = "l2_movies/delete.html"
    success_url = reverse_lazy('movies:list')
