from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'mainapp/index.html', context={
        'message': 'GeekSHOP',
    })


def contact(request):
    menu_links = [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]
    return render(request, 'mainapp/contact.html', context={
        'menu_links': menu_links
    })


def products(request):
    menu_links = [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]
    return render(request, 'mainapp/products.html', context={
        'menu_links': menu_links
    })

