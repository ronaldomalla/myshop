from django.contrib import admin
from .models import Products
from .models import Category
from .models import Customer



class AdminProduct(admin.ModelAdmin):
    list_display =['name', 'price', 'category']






# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)

