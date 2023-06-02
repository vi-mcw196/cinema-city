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
    id_notification = EmailNotificationsSerializer(read_only=True)
    id_screening = ScreeningSerializer(read_only=True)
    owner = UserSerializer(read_only=True)
    seat = ReservedSeatSerializer(read_only=True)

    class Meta:
        model = Reservation
        read_only_fields = ['id_reservation', 'created_at']
        fields = ['id_reservation', 'id_notification', 'id_screening', 'owner', 'seat', 'reservation_status', 'date',
                  'created_at', 'updated_at']
