from django.contrib import admin

from .models import Account, Category, Operation

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Operation)
