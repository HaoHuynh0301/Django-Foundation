from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.gethome, name='index'),
    path('about/', views.getAbout, name='about'),
    path('samplepost/', views.getSamplePost, name='samplePost'),
    path('contact/', views.getContact, name='contact'),
    path('writeblog/', views.getWrite, name='writeblog'),
    path('register/', views.getRegister, name='register'),
    path('login/', views.getLogin, name='login'),
    path('getContactInfor/', views.getContactInfor, name='getContact'),
    path('detail/<int:post_id>/', views.detail, name = 'detail'),
    path('writeblog/createBlog/', views.creatBlog, name = 'createBlog'),
    path('logout/', views.getLogout, name = "logout")
]