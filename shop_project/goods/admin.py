from django.contrib import admin

from .models import *

@admin.register(Categories)  
class CategoriesAdmin(admin.ModelAdmin):  
    list_display = ('name', 'slug')  
    prepopulated_fields = {"slug": ("name", )} 

# admin.site.register(Categories)

# admin.site.register(Products)

@admin.register(Products)  
class ProductsAdmin(admin.ModelAdmin):  
    list_display = ('name', 'slug')  
    prepopulated_fields = {"slug": ("name", )} 