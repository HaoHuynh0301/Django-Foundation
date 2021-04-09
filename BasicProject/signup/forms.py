from django.forms import ModelForm
from . import models

class signUpForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'email']
        
