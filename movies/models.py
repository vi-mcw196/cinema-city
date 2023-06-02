from django.db import models


# Create your models here.
class Movie(models.Model):
    class Category(models.IntegerChoices):
        HORROR = 1, 'HORROR'
        ACTION = 2, 'ACTION'
        COMEDY = 3, 'COMEDY'
        DRAMA = 4, 'DRAMA'
        ROMANCE = 5, 'ROMANCE'

    id_movie = models.AutoField(primary_key=True, db_index=True)
    title = models.CharField(max_length=40, null=True, blank=True)
    producer = models.CharField(max_length=40, null=True, blank=True)
    cast = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=15, choices=Category.choices, default=Category.COMEDY, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-category']

    def __str__(self):
        return self.title

