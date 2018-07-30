from django.db.models import Q
from django.shortcuts import render
from django.views.generic  import (
			DetailView, 
			ListView
			)


from .models import Product
from cart.views import global_cart_detail
from categories.models import Category
from django.db.models import Min, Max


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
		query_price = self.request.GET.get("price", None)
		if query is not None:
			qs = qs.filter(
				Q(name__icontains=query) |
				Q(title__icontains=query) 
				)
		if query_price is not None:
			query_arg = query.split("-")
			qs = qs.filter(
				Q(price__range=(query_arg[0], query_arg[1]))
				).distinct()			
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		context['max_low_price'] = Product.objects.aggregate(Min('price'), Max('price'))
		print(context)

		return context






