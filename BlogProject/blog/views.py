from django.shortcuts import render

# Create your views here.

def gethome(request):
	return render(request, 'home.html')

def getAbout(request):
	return render(request, 'about.html')

def getSamplePost(request):
	return render(request, 'samplepost.html')

def getContact(request):
	return render(request, 'contact.html')

def getWrite(request):
	return render(request, 'writeblog.html')