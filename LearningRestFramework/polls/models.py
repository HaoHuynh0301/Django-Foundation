from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_info(self):
        return 'Name: ' + self.name + ' age: ' + self.age

    def __repr__(self):
        return self.name + ' is added.'