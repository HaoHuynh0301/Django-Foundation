from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.Contact)
admin.site.register(models.Role)
admin.site.register(models.BlogUser)
