from django.db import models
from hack_auth.models import User

# Create your models here.

class INCOME(models.Model):
    INCOME_SOURCE = [
        ('BASE_SALARY', 'BASE_SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('SIDE_HUSTLE', 'SIDE_HUSTLE'),
        ('OTHERS', 'OTHERS') 
    ]

    source = models.CharField(choices=INCOME_SOURCE, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)