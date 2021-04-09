from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.returnAbout, name='about'),
    path('samplepost/', views.returnSamplePost, name='samplepost')
]