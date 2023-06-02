from rest_framework import serializers

from movies.models import Movie


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'producer', 'cast', 'description', 'duration', 'category', 'rating']
