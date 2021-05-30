from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from rest.models import Film


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    text = models.TextField()
    publicationDate = models.DateField(auto_now=True)
