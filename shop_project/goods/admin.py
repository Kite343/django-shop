from django.contrib import admin

from .models import *

# @admin.register(Categories)  
# class CategoriesAdmin(admin.ModelAdmin):  
#     list_display = ('name', 'slug')   

admin.site.register(Categories)

admin.site.register(Products)