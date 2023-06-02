from rest_framework import serializers

from cinema_halls.models import CinemaHall


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ['id_hall', 'hall_number', 'max_seats', 'rows', 'columns']
