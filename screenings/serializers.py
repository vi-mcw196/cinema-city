from rest_framework import serializers

from authentication.models import User
from authentication.serializers import UserSerializer
from cinema_halls.models import CinemaHall
from cinema_halls.serializers import CinemaHallSerializer
from movies.models import Movie
from movies.serializers import MoviesSerializer
from screenings.models import Screening


class ScreeningSerializer(serializers.ModelSerializer):
    id_movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), write_only=True)
    movie_data = MoviesSerializer(source='id_movie', read_only=True)
    id_owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    owner_data = UserSerializer(source='id_owner', read_only=True)
    id_cinema_hall = serializers.PrimaryKeyRelatedField(queryset=CinemaHall.objects.all(), write_only=True)
    cinema_hall_data = CinemaHallSerializer(source='id_cinema_hall', read_only=True)

    class Meta:
        model = Screening
        fields = ['id_screening', 'id_movie', 'movie_data', 'id_owner', 'owner_data', 'id_cinema_hall',
                  'cinema_hall_data', 'screening_time']
