from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, blank = True, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200, null = True)
	email = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length = 200)
	price = models.FloatField()
	digital = models.BooleanField(default = False, blank  =True, null = True)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True, blank = True)
	date_ordered = models.DateTimeField(auto_now_add = True)
	complete = models.BooleanField(default = False)
	transaction_id = models.CharField(max_length = 100, null = True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
	order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
	quantity = models.IntegerField(default = 0, blank = True, null = True)
	date_addded = models.DateTimeField(auto_now_add = True)

class ShippingAddress(models.Model):
	Customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True)
	order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
	address = models.CharField(max_length = 200, null = False)
	state = models.CharField(max_length = 200, null = False)
	zipcode = models.CharField(max_length = 200, null = False)
	date_addded = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.address
