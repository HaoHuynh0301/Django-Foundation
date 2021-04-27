from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 255, blank = True, null = True)
	content = models.CharField(max_length = 5000, blank = True, null = True)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return str(self.id)
	
class Contact(models.Model):
	name = models.CharField(max_length = 255, blank = True, null = True)
	email = models.EmailField(max_length = 255, blank = True, null = True)
	phone = models.IntegerField(blank = True, null = True)
	message= models.CharField(max_length = 2000, blank = True, null = True)

	def __str__(self):
		return str(self.name)