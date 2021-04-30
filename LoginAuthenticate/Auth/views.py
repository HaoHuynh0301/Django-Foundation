from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomCreateForm

# Create your views here.

@login_required(login_url = 'login')
def homePage(request):
    return HttpResponse("Hello")

def loginPage(request):
    context = {}
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print("Done")
        else:
            print("Error")
    return render(request, 'login.html', context)

def registerPage(request):
    forms = CustomCreateForm()
    
    if request.method == 'POST':
        formGet = CustomCreateForm(request.POST)
        if formGet.is_valid():
            print("Valid Form")
            formGet.save()
            return loginPage(request)
            
    context = {
        'form': forms
    }
    
    return render(request, 'Register.html', context)