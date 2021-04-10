from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def returnContact(request):
    return render(request, 'contact/contact.html')

def getPost(request):
    pass