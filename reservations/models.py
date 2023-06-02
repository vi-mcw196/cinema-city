from django.db import models, transaction, DatabaseError
from django.db.models import F

from authentication.models import User
from notifications.models import EmailNotification
from screenings.models import Screening


# Create your models here.
class Seat(models.Model):
    class Type(models.TextChoices):
        STANDARD = 'STANDARD', 'STANDARD'
        VIP = 'VIP', 'VIP'

    id_seat = models.AutoField(primary_key=True, db_index=True)
    seat_type = models.CharField(max_length=8, choices=Type.choices, default=Type.STANDARD)
    seat_code = models.CharField(max_length=100)
    is_reserved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-seat_type']

    def __str__(self):
        return self.seat_code


# TODO: add validation in serializations for each model
# TODO: create, validate and save models in serializers
class Reservation(models.Model):
    class Status(models.TextChoices):
        FREE = 'FREE', 'FREE'
        RESERVED = 'RESERVED', 'RESERVED'
        BOOKED = 'BOOKED', 'BOOKED'

    id_reservation = models.AutoField(primary_key=True, db_index=True)
    id_notification = models.OneToOneField(EmailNotification, on_delete=models.CASCADE)
    id_screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reservation_status = models.CharField(max_length=8, choices=Status.choices, default=Status.FREE)
    date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.pk is not None:
                original = Reservation.objects.get(pk=self.pk)
                if original.version != self.version:
                    raise DatabaseError("The object was modified by another transaction.")
                self.version = F('version') + 1

            result = super().save(*args, **kwargs)

            # Reload the object to ensure the version field was updated correctly
            self.refresh_from_db()

            return result

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return str(self.owner) + 's reservation'
