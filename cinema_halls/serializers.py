from rest_framework import serializers

from cinema_halls.models import CinemaHall


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        read_only_fields = ['id_hall']
        fields = ['id_hall', 'hall_number', 'cinema_hall_type', 'max_seats', 'rows', 'columns']
