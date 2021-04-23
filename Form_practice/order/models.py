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

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True, blank = True)
	date_ordered = models.DateTimeField(auto_now_add = True)
	complete = models.BooleanField(default = False)

	def __str__(self):
		return str(self.id)

	@property
	def get_total_items(self):
		total = sum([item.quantity for item in self.orderitems_set.all()])
		print(total)
		return total

	@property
	def get_total_price(self):
		total_price = sum([item.get_total for item in self.orderitems_set.all()])
		print(total_price)
		return total_price
	


class OrderItems(models.Model):
	product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
	order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
	quantity = models.IntegerField(default = 0, null = True, blank = True)

	def __str__(self):
		return str(self.order.id)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	
