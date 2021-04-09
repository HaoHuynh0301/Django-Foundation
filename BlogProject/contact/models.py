from django.db import models

# Create your models here.

class ContactInformation(models.Model):
    customerID = models.CharField(max_length = 40, primary_key = True)
    name = models.CharField(max_length = 40, null = False)
    email = models.EmailField(max_length = 30, null = False)
    message = models.TextField()
