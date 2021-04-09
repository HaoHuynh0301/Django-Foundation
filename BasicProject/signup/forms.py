from django.forms import ModelForm
from  django import forms
from . import models

class signUpForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'email']

class customSignUpForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 50)
    phone = forms.IntegerField()


        
