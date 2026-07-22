from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other fields you would like to include here

    def __str__(self):
        return self.name


class CarModel(models.Model):
    # Many-to-One relationship to CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # Dealer ID referring to Cloudant database
    dealer_id = models.IntegerField()

    name = models.CharField(max_length=100)

    # Car type choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Feel free to expand choices if desired (e.g., ('COUPE', 'Coupe'))
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SEDAN')

    # Year limited between 2015 and 2023 per instructions
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} - {self.name}"
