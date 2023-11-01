from django.db import models
from hack_auth.models import User
# Create your models here.

class Expense(models.Model):
    CATEGORY_OPTIONS = [
        ('RENT', 'RENT'),
        ('FOOD', 'FOOD'),
        ('TRAVEL','TRAVEL'),
        ('TUITION', 'TUITION'),
        ('ONLINE_SERVICES','ONLINE_SERVICES')
    ]

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.DecimalField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
