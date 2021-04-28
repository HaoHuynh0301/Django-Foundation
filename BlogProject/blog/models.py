from django.db import models
from django.contrib.auth.models import User

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

class Role(models.Model):
    name = models.CharField(max_length = 255, blank = True, null = True)
    
    def __str__(self):
        return self.name
    
class BlogUser(models.Model):
    user = models.OneToOneField(User, blank = True, on_delete = models.CASCADE)
    role = models.ForeignKey(Role, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 255, blank = True, null = True)
    
    def __str__(self):
        return self.user