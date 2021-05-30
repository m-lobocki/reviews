from django.db import models

from rest.models import Profession


class Person(models.Model):
    birthDate = models.DateField()
    birthCountry = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=1, choices=Profession.choices)

    def __str__(self):
        return self.name
