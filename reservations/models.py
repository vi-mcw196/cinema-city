from django.db import models

from authentication.models import User
from notifications.models import EmailNotification
from screenings.models import Screening


# Create your models here.
class ReservedSeat(models.Model):
    class Type(models.IntegerChoices):
        STANDARD = 1, 'STANDARD'
        VIP = 2, 'VIP'

    id_seat = models.AutoField(primary_key=True, db_index=True)
    seat_type = models.CharField(max_length=8, choices=Type.choices, default=Type.STANDARD)
    seat_code = models.CharField(max_length=100)

    class Meta:
        ordering = ['-seat_type']

    def __str__(self):
        return self.seat_code


class Reservation(models.Model):
    class Status(models.IntegerChoices):
        FREE = 1, 'FREE'
        RESERVED = 2, 'RESERVED'
        BOOKED = 3, 'BOOKED'

    id_reservation = models.AutoField(primary_key=True, db_index=True)
    id_notification = models.OneToOneField(EmailNotification, on_delete=models.CASCADE, unique=True)
    id_screening = models.ForeignKey(Screening, on_delete=models.CASCADE, unique=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    seat = models.ForeignKey(ReservedSeat, on_delete=models.CASCADE, unique=True)
    reservation_status = models.CharField(max_length=8, choices=Status.choices, default=Status.FREE)
    date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return str(self.owner) + 's reservation'
