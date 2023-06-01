from django.db import models


# Create your models here.
class Movie(models.Model):
    class Category(models.IntegerChoices):
        HORROR = 1, 'HORROR'
        ACTION = 2, 'ACTION'
        COMEDY = 3, 'COMEDY'
        DRAMA = 4, 'DRAMA'
        ROMANCE = 5, 'ROMANCE'

    id_movie = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    producer = models.CharField(max_length=40)
    cast = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    duration = models.IntegerField()
    category = models.CharField(max_length=6, choices=Category.choices, default=Category.COMEDY)
    rating = models.FloatField()

    class Meta:
        ordering = ['-category']

    def __str__(self):
        return self.title

