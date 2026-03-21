from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import requests

# Create your models here.
class Dog(models.Model):
    SexType = models.TextChoices("SexType", "Female Male")
    StatusType = models.TextChoices("StatusType", 'Adopted Pending Not-Adopted')

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(35)])
    weight = models.FloatField(default=0, validators=[MinValueValidator(0)])
    sex = models.CharField(choices=SexType)
    status = models.CharField(choices=StatusType)
    description = models.CharField(max_length=200)


class Breed(models.Model):
    breed = models.CharField(max_length=100)

    def __str__(self):
        return self.breed