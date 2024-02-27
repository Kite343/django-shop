from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about')
]