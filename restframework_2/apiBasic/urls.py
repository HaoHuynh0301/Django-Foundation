from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('article/', views.ArticleViews.as_view(), name = 'list'),
    path('detail/<int:pk>/', views.ArticleDetail.as_view(), name = 'detail')
]
