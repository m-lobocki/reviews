from django.db import models


class Profession(models.TextChoices):
    ACTOR = 'A'
    DIRECTOR = 'D'
