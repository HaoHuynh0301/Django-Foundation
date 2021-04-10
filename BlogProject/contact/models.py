from django.db import models

# Create your models here.

class ContactInformation(models.Model):
    contactID = models.CharField(max_length = 50, primary_key = True)
    name = models.CharField(max_length = 100, null = False)
    email = models.EmailField(null = False)
    phone = models.CharField(max_length = 13, null = False)
    message = models.CharField(max_length = 200)

    def __str__(self):
        return self.phone

