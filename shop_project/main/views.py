from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'о нас',
        'text_on_page': 'text',
    }
    return render(request, 'main/about.html', context)