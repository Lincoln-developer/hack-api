from django.db import models
from hack_auth.models import User

# Create your models here.

class Income(models.Model):
    income_source = [
        ('BASE_SALARY', 'BASE_SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('SIDE_HUSTLE', 'SIDE_HUSTLE'),
        ('OTHERS', 'OTHERS') 
    ]

    source = models.CharField(choices=income_source, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)

    class Meta:
        ordering:['-date']
    
    def __str__(self):
        return str(self.owner)+'s income'