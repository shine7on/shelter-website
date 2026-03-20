from django.db import models

# Create your models here.
class Dog(models.Model):
    SexType = models.TextChoices("SexType", "Female Male")
    StatusType = models.TextChoices('StatusType', 'Adopted Pending Not-Adopted')

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(choices=SexType)
    status = models.CharField(choices=StatusType)
    description = models.CharField(max_length=200)