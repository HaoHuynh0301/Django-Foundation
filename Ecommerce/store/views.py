from django.shortcuts import render
from . import models
import datetime
import json
from django.http import JsonResponse, HttpResponse

# Create your views here.


def store(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = models.Order.objects.get_or_create(customer = customer, complete = False)
		items = order.orderitem_set.all()	
		cartItems = order.get_cart_items
	else:
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
		items = []
		cartItems  = order['get_cart_items']

	products = models.Product.objects.all()
	context = {'products': products, 'cartItems': cartItems}
	return render(request, 'store/store.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = models.Order.objects.get_or_create(customer = customer, complete = False)
		items = order.orderitem_set.all()	
		cartItems = order.get_cart_items
	else:
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
		items = []
		cartItems  = order['get_cart_items']

	context = {'items': items, 'order': order, 'cartItems': cartItems}

	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = models.Order.objects.get_or_create(customer = customer, complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
		items = []
		cartItems  = order['get_cart_items']

	context = {
		'items': items,
		'order': order,
		'cartItems': cartItems
	}

	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productID = data['productID']
	action = data['action']
	
	customer = request.user.customer
	product = models.Product.objects.get(id = productID)
	order, created = models.Order.objects.get_or_create(customer = customer, complete = False)
	orderitem, created = models.OrderItem.objects.get_or_create(order = order, product = product)

	if action == "add":
		orderitem.quantity = (orderitem.quantity + 1)
	elif action == "remove":
		orderitem.quantity = (orderitem.quantity - 1)
	orderitem.save()

	if orderitem.quantity <= 0:
		orderitem.delete()

	return JsonResponse("Done", safe = False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.load(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = models.Order.objects.get_or_create(customer = customer, complete = False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id

		if total == order.get_cart_total:
			order.complete = True

		order.save()
	return JsonResponse("Payment", safe = False)



































