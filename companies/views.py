from django.db.models import Q
from django.views.generic import (
    DetailView,
    ListView
    )
from companies.models import Company
from cart.views import global_cart_detail
from products.utils import get_category_name
from products.models import Product


def global_companies_detail():
    companies = Company.objects.all()
    return companies


class CompanyDetailView(DetailView):
    def get_queryset(self, *args, **kwargs):
        qs = Company.objects.all()
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(*args, **kwargs)
        context['products'] = Product.objects.filter(company__id=self.kwargs['pk'])
        # context['carts'] = global_cart_detail(self.request)
        # context['category_names'] = get_category_name()
        print(context)
        return context


class CompanyListView(ListView):
    queryset = Company.objects.all()
    template_name = "company_list.html"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = Company.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(price__icontains=query) |
                Q(title__icontains=query)
                )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyListView, self).get_context_data(*args, **kwargs)
        context['carts'] = global_cart_detail(self.request)
        return context
