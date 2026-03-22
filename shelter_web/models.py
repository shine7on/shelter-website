from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Breed(models.Model):
    breed = models.CharField(max_length=100)

    def __str__(self):
        return self.breed
    

    
    
class Dog(models.Model):
    SexType = models.TextChoices("SexType", "Female Male")
    StatusType = models.TextChoices("StatusType", 'Adopted Pending Not-Adopted')
    class UnitType(models.TextChoices):
        KG = 'kg', 'Kilograms (kg)',
        LB = 'lb', 'Pounds (lb)',
        G = 'g', 'Grams (g)'

    name = models.CharField(max_length=100)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    age = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(35)])
    weight = models.FloatField(default=0, validators=[MinValueValidator(0)])
    weight_unit = models.CharField(default=' kg',choices=UnitType)
    sex = models.CharField(choices=SexType)
    status = models.CharField(choices=StatusType)
    description = models.CharField(max_length=200)
