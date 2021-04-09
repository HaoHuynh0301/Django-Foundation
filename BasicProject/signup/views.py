from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def Index(request):
    form = forms.signUpForm()

    context_form = {
        'form': form
    }
    return render(request, 'signup/signupform.html', context_form)

def view_404_error(request, exception):
    return render(request, '404.html')

def getSignUpPost(request):
    if request.method == "POST":
        data = forms.signUpForm(request.POST)
        Res = False
        if data.is_valid():
            Res = True;
        
        context_signup = {
            'Res': Res
        }
        
    return render(request, 'signup/signuppost.html', context_signup)
