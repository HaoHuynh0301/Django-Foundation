from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
import random, string

# Create your views here.

def returnContact(request):
    return render(request, 'contact/contact.html')

def getPost(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            tmpContactID = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
            tmpName = form.cleaned_data['name']
            tmpEmail = form.cleaned_data['email']
            tmpPhone = form.cleaned_data['phone']
            tmpMessage = form.cleaned_data['message']
            newContact = models.ContactInformation(contactID = tmpContactID, name = tmpName, phone = tmpPhone, email = tmpEmail, message = tmpMessage)
            newContact.save()
            return render(request, 'contact/contact.html')
    return render(request, 'contact/contact.html', context)