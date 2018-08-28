from django.db.models import Q
from django.views.generic import (
			DetailView, 
			ListView
			)
from .models import Product
from cart.views import global_cart_detail
from tickets.views import global_ticket_detail
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
		context['tickets'] = global_ticket_detail(*args)
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
			query_arg = query_price.split("TL-")
			min_value = query_price.split("TL-")[0]
			max_value = query_arg[1].split("TL")[0]
			qs = qs.filter(
				Q(price__range=(min_value, max_value))
				).distinct()				
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		context['max_min_price'] = self.price_list_min_max()
		return context

	@staticmethod
	def price_list_min_max():
		price__min = round(Product.objects.aggregate(Min('price'))['price__min'])
		price__max = round(Product.objects.aggregate(Max('price'))['price__max'])
		price_list = {'price__min': price__min, 'price__max': price__max}
		return price_list
