from django.shortcuts import render
from .temp.goods_list import goods

def catalog(request):
    context = {
        'title': 'Home - catalog',
        'goods': goods

    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')