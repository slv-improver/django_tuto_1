from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    class Season(models.TextChoices):
        SUMMER = 'SU'
        FALL = 'FA'
        WINTER = 'WI'
        SPRING = 'SP'

    name = models.fields.CharField(max_length=100)
    year = models.fields.IntegerField(
        default=2000,
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    season = models.fields.CharField(choices=Season.choices, max_length=5)
    comestible = models.fields.BooleanField(default=True)
    wikipedia = models.fields.URLField(null=True, blank=True)

class Listing(models.Model):

    class Type(models.TextChoices):
        CLOTHING = 'CL'
        GAMING = 'GA'
        HOME = 'HO'
        MISCELLANEOUS = 'M'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        default=2000,
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    type = models.fields.CharField(choices=Type.choices, max_length=6)
