from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

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
    birthday = models.DateField(null=True, blank=True)
    age_year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(35)])
    age_month = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(11)])
    weight = models.FloatField(default=0, validators=[MinValueValidator(0)])
    weight_unit = models.CharField(default='kg',choices=UnitType)
    sex = models.CharField(max_length=6, choices=SexType)
    status = models.CharField(max_length=11, choices=StatusType)
    description = models.TextField(max_length=200)

    photo = models.ImageField(upload_to='dogs/', null=True, blank=True)

    # model-level validation
    def clean(self):
        if self.birthday == None and self.age_year == None and self.age_month == None:
            raise ValidationError('Add either birthday or age (year/month)')
        elif self.age_year < 0 or not 0 <= self.age_month <= 12:
            raise ValidationError('Invalid Value')
    
    # gives name instead of dog_object
    def __str__(self):
        return self.name