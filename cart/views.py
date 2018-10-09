from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart
from cart.forms import CartAddProductForm
from projectMarket.settings.local import EMAIL_HOST_USER
from django.core.mail import send_mail


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


def cart_opt(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.update(product)
    return redirect('cart:cart_detail')


def global_cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return cart


def send_mail_cart(request):
    try:
        send_mail("selam", "", EMAIL_HOST_USER, ["testuser@gmail.com"], fail_silently=False)
    except:
        raise BaseException("E-posta gönderilirken bir hata oluştu.")