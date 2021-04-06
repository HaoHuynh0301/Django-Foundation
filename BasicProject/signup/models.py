from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 100, null = False, primary_key = True)
    email= models.CharField(max_length = 100, null=True)
    phone = models.CharField(max_length = 12)
    
    def __str__(self):
        return self.name
