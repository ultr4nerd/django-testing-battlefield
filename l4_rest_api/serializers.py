"""REST API level app serializers"""

from rest_framework import serializers

from l2_movies.models import Movie, Director


class MovieSerializer(serializers.ModelSerializer):
    """Serializer for Movie model"""

    class Meta:
        model = Movie
        fields = "__all__"


class DirectorSerializer(serializers.ModelSerializer):
    """Serializer for Director model"""

    class Meta:
        model = Director
        fields = "__all__"
