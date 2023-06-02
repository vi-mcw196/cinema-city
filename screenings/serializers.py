from rest_framework import serializers

from authentication.serializers import UserSerializer
from cinema_halls.serializers import CinemaHallSerializer
from movies.serializers import MoviesSerializer
from screenings.models import Screening


class ScreeningSerializer(serializers.ModelSerializer):
    id_movie = MoviesSerializer()
    id_owner = UserSerializer()
    id_cinema_hall = CinemaHallSerializer()

    class Meta:
        model = Screening
        fields = ['id_screening', 'id_movie', 'id_owner', 'id_cinema_hall', 'screening_time']
