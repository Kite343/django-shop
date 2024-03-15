# from django.contrib import admin
from django.urls import include, path


from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about')
]