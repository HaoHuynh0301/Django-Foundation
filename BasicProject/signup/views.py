from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def Index(request):
    form = forms.signUpForm()

    context = {
        'form': form
    }
    return render(request, 'signup/signup.html', context)

def view_404_error(request, exception):
    return render(request, '404.html')

def getSignUpPost(request):
    if request.method == "POST":
        res = False
        signUpForm = forms.signUpForm(request.POST)

        if signUpForm.is_valid():
            res = True
            signUpForm.save()
            return HttpResponse("Done")

        else:
            return HttpResponse("False")
