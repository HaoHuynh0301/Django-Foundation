from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/employee/(?P<pk>[0-9]+)$',
        views.get_delete_update_employee,
        name='get_delete_update_employee'
    ),
    url(
        r'^api/employee/$',
        views.get_post_employee,
        name='get_post_employee'
    )
]
