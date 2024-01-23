from django.contrib import admin

from .models import Category, Operation, Period, BankAccount

admin.site.register(Category)
admin.site.register(Operation)
admin.site.register(Period)
admin.site.register(BankAccount)
