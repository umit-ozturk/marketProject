from django.db.models import Q
from django.shortcuts import render
from django.views.generic  import (
			DetailView, 
			ListView
			)


from .models import Aktuel

# Create your views here.

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