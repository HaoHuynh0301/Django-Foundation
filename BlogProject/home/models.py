from django.db import models

# Create your models here.

class Post(models.Model):
	postID = models.CharField(max_length = 10, primary_key = True)
	title = models.CharField(max_length = 30, null = False)
	content = models.CharField(max_length = 3000)
	date = models.DateTimeField(auto_now  = True)

	def __str__(self):
		return self.title