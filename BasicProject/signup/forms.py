from django.forms import ModelForm
from django import forms
from . import models

class signUpForm(ModelForm):
    name = forms.CharField(max_length = 100)
    email= forms.CharField(max_length = 100)
    phone = forms.CharField(max_length = 12)
    class Meta:
        model = models.Customer
        fields = ['name', 'email', 'phone']
        
