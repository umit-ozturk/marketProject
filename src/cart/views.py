from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from products.models import Product
from accounts.models import UserProfile
from .cart import Cart
from cart.forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail', kwargs={'id':product_id})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request, account_name):
	cart = Cart(request)
	user = get_object_or_404(UserProfile, user__username=account_name)
	if not request.user or not request.user.is_superuser:
		raise Http404
	print(user.__dict__)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
	return render(request, 'carts/detail.html', {'cart': cart})
