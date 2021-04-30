from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "auth"

urlpatterns = [
    path('', views.homePage, name = "home"),
    path('login/', views.loginPage, name = "login"),
    path('register/', views.registerPage, name = "register")
]
