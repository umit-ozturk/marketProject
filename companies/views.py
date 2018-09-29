from django.db.models import Q
from django.views.generic import (
			DetailView, 
			ListView
			)


from .models import Company
from cart.views import global_cart_detail


class CompanyDetailView(DetailView):
	queryset = Company.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(CompanyDetailView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context


class CompanyListView(ListView):
	queryset = Company.objects.all()
	template_name = "company_list.html"

	def get_queryset(self, *args, **kwargs):
		qs = Company.objects.all()
		query = self.request.GET.get("q", None)

		if query is not None:
			qs = qs.filter(
				Q(name__icontains=query) |
				Q(price__icontains=query) |
				Q(title__icontains=query)
				)
		print(qs.count())
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(CompanyListView, self).get_context_data(*args, **kwargs)
		context['carts'] = global_cart_detail(self.request)
		return context
