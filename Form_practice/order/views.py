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
	if request.user.is_authenticated:
		customer = request.user.customer
		# order, created = models.Order.objects.get_or_create(customer = customer, complete = False)
		order, created = models.Order.objects.get_or_create(customer = customer, complete = False)
		orderitems = order.orderitems_set.all()
		cardItems = order.get_total_items
		totalPrice = order.get_total_price
	else:
		print("error")

	context = {'orderitems': orderitems, 'totalitems': cardItems, 'order': order, 'totalprice': totalPrice}

	return render(request, 'checkout.html', context)