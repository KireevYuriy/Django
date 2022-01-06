from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from cartapp.models import Cart
from mainapp.models import Product

def cart(request):
    content = {}
    return render(request, 'cartapp/cart.html', content)


def add_to_cart(request, pk):

    product = get_object_or_404(Product, pk=pk)
    cart_product = request.user.cart.filter(id=pk).first()
    if not cart_product:
        cart_product = Cart(user=request.user, product=product)
    cart_product.quantity += 1
    cart_product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart (request, pk):
    content = {}
    return render(request, 'cartapp/cart.html', content)
