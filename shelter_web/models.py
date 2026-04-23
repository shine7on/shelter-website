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
    

class Adoptation(models.Model):
    HousingType = models.TextChoices('Housing', 'House Apartment Condo Townhouse Other')
    YardType = models.TextChoices('Yard', 'yes_fenced yes_unfenced No')
    StateType = models.TextChoices('State', 
        'AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY'
    )

    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    street = models.CharField(blank=False)
    city = models.CharField(blank=False)
    state = models.CharField(default='', choices=StateType, blank=False)
    zip = models.CharField(default='', blank=False)
    # state = models.CharField(blank=False, choices=)
    email = models.EmailField(blank=False)
    interested_dog = models.CharField(blank=False)
    phone = models.CharField(max_length=15, blank=False)
    housing = models.CharField(default='', choices=HousingType)
    yard = models.CharField(default='', choices=YardType)
    comment = models.CharField(blank=True)