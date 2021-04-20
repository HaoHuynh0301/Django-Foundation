from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, blank = True, on_delete=models.CASCADE)
	name = models.CharField(max_length = 255, null = True)
	email = models.EmailField(blank = True, null = True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=255, blank = False)
	price = models.FloatField()
	image = models.ImageField(null = True, blank = True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
