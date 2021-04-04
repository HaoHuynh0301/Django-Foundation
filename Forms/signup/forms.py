from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(maxlength=100, label='name')
    email = forms.EmailFieldField(maxlength=100, label='email')
    phone = forms.IntegerField()