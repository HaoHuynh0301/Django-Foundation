from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100, label='name', widget=forms.TextInput)
    email = forms.CharField(max_length=100, label='email', widget=forms.TextInput)
    phone = forms.CharField(max_length=12, widget=forms.TextInput)