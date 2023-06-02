from rest_framework import serializers

from movies.models import Movie


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        read_only_fields = ['id_movie']
        fields = ['id_movie', 'title', 'producer', 'cast', 'description', 'duration', 'category', 'rating']

    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError('Rating has to be between 1 and 10.')
        return value
