from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'price', 'stock', 'available']
    list_editable = ['price', 'stock', 'available']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
