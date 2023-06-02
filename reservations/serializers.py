from rest_framework import serializers

from authentication.serializers import UserSerializer
from notifications.serializers import EmailNotificationsSerializer
from reservations.models import Reservation, ReservedSeat
from screenings.serializers import ScreeningSerializer


class ReservedSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservedSeat
        read_only_fields = ['id_seat']
        fields = ['id_seat', 'seat_type', 'seat_code']


class ReservationSerializer(serializers.ModelSerializer):
    id_notification = EmailNotificationsSerializer()
    id_screening = ScreeningSerializer()
    owner = UserSerializer()
    seat = ReservedSeatSerializer()

    class Meta:
        model = Reservation
        read_only_fields = ['id_reservation', 'created_at']
        fields = ['id_reservation', 'id_notification', 'id_screening', 'owner', 'seat', 'reservation_status', 'date',
                  'created_at', 'updated_at', 'version']

    def create(self, validated_data):
        # Retrieve the screening from the validated data
        screening = validated_data.get('id_screening')

        # Retrieve the cinema hall from the screening
        cinema_hall = screening.id_cinema_hall

        # Retrieve the current number of reservations for this screening
        reservation_count = Reservation.objects.filter(id_screening=screening).count()

        # Compare the current reservation count with the max_seats of the cinema hall
        if reservation_count >= cinema_hall.max_seats:
            raise serializers.ValidationError(
                "The number of reserved seats cannot exceed the maximum seats of the cinema hall.")

        # Create the reservation
        reservation = Reservation.objects.create(**validated_data)

        return reservation
