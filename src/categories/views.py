from django.db.models import Q
from django.shortcuts import render
from django.views.generic  import (
			DetailView, 
			ListView
			)


from .models import Category
from cart.views import global_cart_detail

# Create your views here.

class CategoryListView(ListView):
	queryset = Category.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Category.objects.all()
		#query = self.request.GET.get("q", None)
		#if query is not None:
		#	qs = qs.filter(
		#		Q(name__icontains=query) |
		#		Q(price__icontains=query) |
		#		Q(title__icontains=query)
		#		)
		return qs


	def get_context_data(self, *args, **kwargs):
		context = super(CategoryListView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context



class CategoryDetailView(DetailView):
	queryset = Category.objects.all()
	def get_queryset(self, *args, **kwargs):
		qs = Category.objects.all()
		return qs


	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context