from django.shortcuts import render
from . import models

# Create your views here.


def store(request):
	products = models.Product.objects.all()
	context = {'products': products}
	return render(request, 'store/store.html', context)

def cart(request):
	return render(request, 'store/cart.html')

def checkout(request):
	return render(request, 'store/checkout.html')

