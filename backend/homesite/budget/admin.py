from django.contrib import admin

from .models import Category, Operation, Period

admin.site.register(Category)
admin.site.register(Operation)
admin.site.register(Period)
