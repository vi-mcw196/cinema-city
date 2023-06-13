from rest_framework import serializers

from cinema_city.settings import MIN_SEATS, MAX_SEATS, MIN_ROWS_COLUMNS, MAX_ROWS_COLUMNS
from cinema_halls.models import CinemaHall


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        read_only_fields = ['id_hall']
        fields = ['id_hall', 'hall_number', 'cinema_hall_type', 'max_seats', 'rows', 'columns']

    def validate_max_seats(self, value):
        if value < MIN_SEATS or value > MAX_SEATS:
            raise serializers.ValidationError('Max seats has to be between 1 and 10.')
        return value

    def validate_rows(self, value):
        if value < MIN_ROWS_COLUMNS or value > MAX_ROWS_COLUMNS:
            raise serializers.ValidationError('Rows has to be between 1 and 10.')
        return value

    def validate_columns(self, value):
        if value < MIN_ROWS_COLUMNS or value > MAX_ROWS_COLUMNS:
            raise serializers.ValidationError('Columns has to be between 1 and 10.')
        return value
