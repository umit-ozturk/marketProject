from django.db.models import Q
from django.shortcuts import render
from django.views.generic  import (
			DetailView, 
			ListView
			)


from .models import Aktuel, AktuelProducts

# Create your views here.


class AktuelProductListView(ListView):
	queryset = AktuelProducts.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = AktuelProducts.objects.all()

		return qs

class AktuelProductDetailView(DetailView):
	queryset = AktuelProducts.objects.all()

	def get_queryset(self, *args, **kwargs):
		
		qs = AktuelProducts.objects.filter(pk=pk)
		if qs.exists():
			return qs
		return None

class AktuelListView(ListView):
	queryset = Aktuel.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Aktuel.objects.all()

		return qs

class AktuelDetailView(DetailView):
	queryset = Aktuel.objects.all()

	def get_queryset(self, *args, **kwargs):
		aktuel_slug = self.kwargs.get("slug")
		
		qs = Aktuel.objects.filter(slug=aktuel_slug)
		if qs.exists():
			return qs
		return None
