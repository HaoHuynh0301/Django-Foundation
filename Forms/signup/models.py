from django.db import models

# Create your models here.

class Customer(models.Model):

    def __name__(self):
        return self.name

    name = models.CharField(max_length = 50, primary_key = True)
    email = models.EmailField(max_length = 50)
    phone = models.IntegerField(max_length = 12)
