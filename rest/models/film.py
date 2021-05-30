from django.db import models

from rest.models import Person


class Film(models.Model):
    director = models.ForeignKey(Person, on_delete=models.RESTRICT, related_name='films_created')
    title = models.CharField(max_length=100)
    description = models.TextField()
    releaseDate = models.DateField()
    actors = models.ManyToManyField(Person, related_name='films_played_in')
