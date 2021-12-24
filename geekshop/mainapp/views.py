from django.shortcuts import render
from .models import Product, ProductCategory
from django.shortcuts import get_object_or_404

MENU_LINKS = [
        {'href': 'index', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]

def index(request):
    # products = [
    #     {
    #         'name': 'Квантовая лампа',
    #         'description': 'Светодиодная лампа',
    #         'image_path': 'img/product-1.jpg',
    #     },
    #     {
    #         'name': 'Стул синий',
    #         'description': 'Стул со спинкой мягкий, синий.',
    #         'image_path': 'img/product-2.jpg',
    #     }
    # ]
    products = Product.objects.all()
    return render(request, 'mainapp/index.html', context={
        'title': 'Магазин',
        'content_block_class': 'slider',
        'menu_links': MENU_LINKS,
        'products': products,
    })


def contact(request):

    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'content_block_class': 'hero',
        'menu_links': MENU_LINKS
    })


def products(request, pk=None):
    if not pk:
        select_category = ProductCategory.objects.first()
    else:
        select_category = get_object_or_404(ProductCategory, id=pk)
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(category=select_category)
    return render(request, 'mainapp/products.html', context={
        'title': 'Каталог',
        'content_block_class': 'hero-white',
        'menu_links': MENU_LINKS,
        'select_category': select_category,
        'categories': categories,
        'products': products,
    })

