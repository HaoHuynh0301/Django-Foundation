from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('updateitem/', views.updateItem, name="updateitem")
]
