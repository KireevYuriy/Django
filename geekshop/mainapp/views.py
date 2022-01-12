from django.shortcuts import render
from .models import Product, ProductCategory, ProductManager
from django.shortcuts import get_object_or_404
from django.urls import reverse


MENU_LINKS = [
    {"href": "index", "active_if": ["index"], "name": "домой"},
    {
        "href": "products:index",
        "active_if": ["products:index", "products:category"],
        "name": "продукты",
    },
    {"href": "contact", "active_if": ["contact"], "name": "контакты"},
]


def index(request):
    products = Product.objects.all()[:4]
    return render(
        request,
        "mainapp/index.html",
        context={
            "title": "Магазин",
            "content_block_class": "slider",
            "menu_links": MENU_LINKS,
            "products": products,
        },
    )


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
            "content_block_class": "hero",
            "menu_links": MENU_LINKS,

        },
    )

def products_index(request):
    select_category_dict = {'name': 'Всё', 'href': reverse('products:index')}
    categories = [{'name': c.name, 'href': reverse('products:category', args=[c.id])} for c in
                  ProductCategory.objects.all()]
    categories = [{'name': 'Всё', 'href': reverse('products:index')}, *categories]
    products = Product.objects.all().order_by('price')[:3]
    return render(
        request,
        "mainapp/products_list.html",
        context={
            "title": "Каталог",
            "content_block_class": "hero-white",
            "menu_links": MENU_LINKS,
            "select_category": select_category_dict,
            "categories": categories,
            "hot_product": ProductManager.hot_product,
            "products": products,
        },
    )


def products(request, pk=None):
    select_category = get_object_or_404(ProductCategory, id=pk)
    select_category_dict = {
        'name': select_category.name,
        'href': reverse('products:category', args=[select_category.id])}

    categories = [{'name': c.name, 'href': reverse('products:category', args=[c.id])} for c in
                  ProductCategory.objects.all()]
    categories = [{'name': 'Всё', 'href': reverse('products:index')}, *categories]
    products = Product.objects.filter(category=select_category).order_by("price")
    return render(
        request,
        "mainapp/products_list.html",
        context={
            "title": "Каталог",
            "content_block_class": "hero-white",
            "menu_links": MENU_LINKS,
            "select_category": select_category_dict,
            "categories": categories,
            "products": products,

        },
    )
