from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 255, label = 'name', widget=forms.TextInput)
	email = forms.EmailField(max_length = 255, label = 'email', widget=forms.TextInput)
	phone = forms.IntegerField(label = 'phone', widget = forms.TextInput)
	message = forms.CharField(max_length = 2000, label = 'message', widget = forms.TextInput)
 
class PostForm(forms.Form):
    title = forms.CharField(max_length = 255, label = 'title', widget = forms.TextInput)
    content = forms.CharField(max_length = 5000, label = 'content', widget = forms.Textarea)
    
class CreateUserForms(UserCreationForm):
    class Meta:
			model = User
			fields = ['username', 'email', 'password1', 'password2']
	