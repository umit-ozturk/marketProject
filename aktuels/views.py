from django.db.models import Q
from django.shortcuts import render
from django.views.generic  import (
			DetailView, 
			ListView
			)


from .models import Aktuel, AktuelProducts
from cart.views import global_cart_detail

# Create your views here.


class AktuelProductListView(ListView):
	queryset = AktuelProducts.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = AktuelProducts.objects.all()

		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(AktuelProductListView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context		

class AktuelProductDetailView(DetailView):
	queryset = AktuelProducts.objects.all()

	def get_queryset(self, *args, **kwargs):
		
		qs = AktuelProducts.objects.filter(pk=pk)
		if qs.exists():
			return qs
		return None

	def get_context_data(self, *args, **kwargs):
		context = super(AktuelProductDetailView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context		

class AktuelListView(ListView):
	queryset = Aktuel.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Aktuel.objects.all()

		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(AktuelListView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context

class AktuelDetailView(DetailView):
	queryset = Aktuel.objects.all()

	def get_queryset(self, *args, **kwargs):
		aktuel_slug = self.kwargs.get("slug")
		
		qs = Aktuel.objects.filter(slug=aktuel_slug)
		if qs.exists():
			return qs
		return None

	def get_context_data(self, *args, **kwargs):
		context = super(AktuelDetailView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context