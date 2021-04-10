from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    phone = forms.CharField(max_length = 13)
    message = forms.CharField(widget=forms.Textarea)