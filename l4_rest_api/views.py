"""REST API level app views"""

from rest_framework import viewsets

from .serializers import MovieSerializer, DirectorSerializer
from l2_movies.models import Movie, Director


class MovieViewSet(viewsets.ModelViewSet):
    """Viewset for Movie model"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    """Viewset for Director model"""
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
