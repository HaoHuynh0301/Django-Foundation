from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):
    return HttpResponse("Hello")

def view_404_error(request, exception):
    return render(request, '404.html')
