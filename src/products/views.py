from django.db.models import Q
from django.shortcuts import render
from django.views.generic  import (
			DetailView, 
			ListView
			)


from .models import Product
from cart.cart import Cart
from cart.forms import CartAddProductForm


class ProductDetailView(DetailView):
	queryset = Product.objects.all()



class ProductListView(ListView):
	queryset = Product.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Product.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(name__icontains=query) |
				Q(price__icontains=query) |
				Q(title__icontains=query)
				)
		return qs


	def cart(self):
		cart = Cart(self.request)
		for item in cart:
			item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})		
		return cart



	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		cart_product_form = CartAddProductForm
		context['carts'] = self.cart()
		context[cart_product_form] = cart_product_form
		return context
