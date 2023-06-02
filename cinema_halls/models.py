from django.db import models

from authentication.models import User
from movies.models import Movie


# Create your models here.
class CinemaHall(models.Model):
    id_hall = models.AutoField(primary_key=True, db_index=True)
    hall_number = models.IntegerField(null=True, blank=False)
    max_seats = models.IntegerField(null=True)
    rows = models.IntegerField(null=False)
    columns = models.IntegerField(null=False)

    class Meta:
        ordering: ['-id_hall']

    def __str__(self):
        return str(self.hall_number) + 's CinemaHall'
