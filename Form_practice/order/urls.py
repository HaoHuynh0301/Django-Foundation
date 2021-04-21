from django.contrib import admin
from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.Home, name='home'),
    path('checkout/', views.Checkout, name='checkout')
]


