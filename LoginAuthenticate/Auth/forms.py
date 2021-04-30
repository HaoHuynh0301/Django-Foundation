from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'email', 'password2']

