from django.db import models

from authentication.models import User
from movies.models import Movie


# Create your models here.
class CinemaHall(models.Model):
    class Type(models.TextChoices):
        TWO_D = '2D', '2D'
        THREE_D = '3D', '3D'
        IMAX = 'IMAX', 'IMAX'
        VIP = 'VIP', 'VIP'

    id_hall = models.AutoField(primary_key=True, db_index=True)
    hall_number = models.IntegerField(null=True, blank=False)
    cinema_hall_type = models.CharField(max_length=15, choices=Type.choices, default=Type.TWO_D, null=True, blank=True)
    max_seats = models.IntegerField(null=True)
    rows = models.IntegerField(null=False)
    columns = models.IntegerField(null=False)

    class Meta:
        ordering = ['-id_hall']

    def __str__(self):
        return str(self.hall_number) + 's CinemaHall'
