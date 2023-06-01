from django.db import models

from movies.models import Movie
from authentication.models import User


# Create your models here.
class CinemaHall(models.Model):
    id_hall = models.AutoField(primary_key=True)
    hall_number = models.IntegerField()
    max_seats = models.IntegerField()
    rows = models.IntegerField()
    columns = models.IntegerField()

    class Meta:
        ordering: ['-id_hall']

    def __str__(self):
        return str(self.hall_number) + 's CinemaHall'


class Screening(models.Model):
    id_screening = models.AutoField(primary_key=True)
    id_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    id_owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    id_cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    screening_time = models.DateTimeField()

    class Meta:
        ordering = ['-id_screening']

    def __str__(self):
        return str(self.screening_time) + 's time of ' + self.id_movie.title + ' movie '
