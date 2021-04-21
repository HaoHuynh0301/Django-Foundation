from django.shortcuts import render
from . import models

# Create your views here.


def Home(request):
	product = models.Product.objects.all()
	context = {
		'products': product
	}
	return render(request, 'home.html', context)

def Checkout(request):
	return render(request, 'checkout.html')