from django.core.mail import send_mail
from django.db import transaction
from rest_framework import serializers

from authentication.models import User
from authentication.serializers import UserSerializer
from cinema_city import settings
from notifications.serializers import EmailNotificationsSerializer
from reservations.models import Reservation, Seat, TempReservation
from screenings.models import Screening
from screenings.serializers import ScreeningSerializer
from datetime import timedelta
from django.utils import timezone


class ReservedSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        read_only_fields = ['id_seat']
        fields = ['id_seat', 'seat_type', 'seat_code', 'is_reserved']


class ReservationSerializer(serializers.ModelSerializer):
    # id_notification = EmailNotificationsSerializer()
    id_screening = serializers.PrimaryKeyRelatedField(queryset=Screening.objects.all(), write_only=True)
    screening_data = ScreeningSerializer(source='id_screening', read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    owner_data = UserSerializer(source='owner', read_only=True)
    seat = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all(), write_only=True)
    seat_data = ReservedSeatSerializer(source='seat', read_only=True)

    class Meta:
        model = Reservation
        read_only_fields = ['id_reservation', 'created_at']
        fields = [
            'id_reservation',
            'id_screening',
            'screening_data',
            'owner',
            'owner_data',
            'seat',
            'seat_data',
            'reservation_status',
            'date',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        screening_data = validated_data['id_screening']
        screening_serializer = ScreeningSerializer(data=screening_data)
        screening_serializer.is_valid(raise_exception=True)
        screening = screening_serializer.save()

        seat_data = validated_data['seat']
        seat_serializer = ReservedSeatSerializer(data=seat_data)
        seat_serializer.is_valid(raise_exception=True)
        seat = seat_serializer.save()
        cinema_hall = screening.id_cinema_hall

        reservation_count = Reservation.objects.filter(id_screening=screening).count()

        if reservation_count >= cinema_hall.max_seats:
            raise serializers.ValidationError(
                "The number of reserved seats cannot exceed the maximum seats of the cinema hall.")

        try:
            with transaction.atomic():
                # Set reservation status as 'RESERVED'
                validated_data['reservation_status'] = Reservation.Status.RESERVED

                temp_reservations = TempReservation.objects.filter(seat=seat, screening=screening)
                temp_reservations = temp_reservations.filter(created_at__gte=timezone.now() - timedelta(minutes=15))
                if temp_reservations.exists():
                    raise serializers.ValidationError("This seat is temporarily reserved.")

                if (
                        Reservation.objects.filter(seat=seat, screening=screening).exists()
                        or seat.is_reserved
                ):
                    raise serializers.ValidationError("This seat is already reserved.")

                # Mark seat as reserved
                seat.is_reserved = True
                seat.save()

                if self.instance is not None:
                    timediff = timezone.now() - self.instance.created_at
                    if timediff.seconds > settings.TENTATIVE_BOOKED_SEC:
                        raise serializers.ValidationError('Reservation session expired.')

                reservation = Reservation.objects.create(**validated_data)

                # If reservation was successful, set reservation status to 'BOOKED'
                reservation.reservation_status = Reservation.Status.BOOKED
                reservation.save()

                send_mail(
                    'Your reservation',
                    'You have successfully made a reservation.',
                    'from@example.com',
                    [validated_data['owner'].email],
                    fail_silently=False,
                )

                return reservation

        except Exception as e:
            transaction.rollback()
            raise serializers.ValidationError(str(e))

    def update(self, instance, validated_data):
        screening_data = validated_data.pop('id_screening')
        screening_serializer = ScreeningSerializer(instance.id_screening, data=screening_data, partial=True)
        screening_serializer.is_valid(raise_exception=True)
        screening_serializer.save()

        seat_data = validated_data.pop('seat')
        seat_serializer = ReservedSeatSerializer(instance.seat, data=seat_data, partial=True)
        seat_serializer.is_valid(raise_exception=True)
        seat_serializer.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
