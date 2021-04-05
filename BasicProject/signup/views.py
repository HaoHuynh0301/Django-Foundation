from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):
    context = {
        
    }
    return render(request, 'signup/signup.html', context)

def view_404_error(request, exception):
    return render(request, '404.html')
