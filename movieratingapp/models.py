from __future__ import unicode_literals
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=500)
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
    def __str__(self):
        return self.name

class Images(models.Model):
    poster = models.ImageField(default='default.jpg',upload_to='images/')

class Movie(models.Model):
    name = models.CharField(max_length=500)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    poster_fk = models.ForeignKey(Images, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre)
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
    def __str__(self):
        return self.name
