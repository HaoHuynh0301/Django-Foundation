from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):
    return render(request, 'home/mainContent.html')

def returnAbout(request):
    return render(request, 'about.html')

def returnSamplePost(request):
    return render(request, 'samplepost.html')

