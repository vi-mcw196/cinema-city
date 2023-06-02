from django.db import models

from authentication.models import User
from cinema_halls.models import CinemaHall
from movies.models import Movie


# Create your models here.
class Screening(models.Model):
    id_screening = models.AutoField(primary_key=True, db_index=True)
    id_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    id_owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    id_cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    screening_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id_screening']

    def __str__(self):
        return str(self.screening_time) + 's time of ' + self.id_movie.title + ' movie '
