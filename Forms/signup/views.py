from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . import models, forms

# Create your views here.

def Index(request):
            
    return render(request, 'signup.html')

def GetSignUp(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            tmpName = request.POST['name']
            tmpEmail = request.POST['email']
            tmpPhone = request.POST['phone']
            newCus = models.Customer(name=tmpName, email=tmpEmail, phone=tmpPhone)
            newCus.save()
            return HttpResponse("Done")
    return HttpResponse("Error")