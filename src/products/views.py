from django.db.models import Q
from django.shortcuts import render
from django.views.generic  import (
			DetailView, 
			ListView
			)


from .models import Product
from cart.views import global_cart_detail
from categories.models import Category


class ProductDetailView(DetailView):
	queryset = Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context



class ProductListView(ListView):
	queryset = Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context


class SearchProductListView(ListView):
	template_name = 'products/search_product_list.html'
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

	def get_context_data(self, *args, **kwargs):
		context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		context['categories'] = Category.objects.all()
		print(context['categories'].__dict__)
		return context