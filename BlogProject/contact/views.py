from django.shortcuts import render

# Create your views here.

def returnContact(request):
    return render(request, 'contact/contact.html')