from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.gethome, name='index'),
    path('about/', views.getAbout, name='about'),
    path('samplepost/', views.getSamplePost, name='samplePost'),
    path('contact/', views.getContact, name='contact'),
    path('writeblog/', views.getWrite, name='writeblog')
]