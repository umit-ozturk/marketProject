from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from products.models import Product
from .cart import Cart
from cart.forms import CartAddProductForm



def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = global_cart_detail(request)
    return render(request, 'carts/detail.html', {'carts': cart})




###### 

def global_cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return cart