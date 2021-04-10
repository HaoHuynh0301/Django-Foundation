from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.returnContact, name='contact'),
    path('contactget/', views.getPost, name="getPost")
]