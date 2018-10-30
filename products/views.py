from django.db.models import Q
from django.views.generic import (
            DetailView,
            ListView,
            TemplateView
            )
from .models import Product
from companies.views import global_companies_detail
from categories.models import Category
from cart.views import global_cart_detail
from tickets.views import global_ticket_detail
from django.db.models import Min, Max
from products.api.views import ProductSlugAPIView


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
        context['companies'] = global_companies_detail(*args)
        return context


    @staticmethod
    def get_min_price():
        price__min = round(Product.objects.aggregate(Max('price'))['price__max'])
        return price__min

    @staticmethod
    def get_max_price():
        price__max = round(Product.objects.aggregate(Max('price'))['price__max'])
        return price__max


class SearchProductListView(ListView):
    template_name = 'products/search_product_list.html'
    qs_id_list = ProductSlugAPIView.product_for_slug_min_price()
    queryset = Product.objects.filter(id__in=qs_id_list)

    def get_queryset(self, *args, **kwargs):
        qs_id_list = ProductSlugAPIView.product_for_slug_min_price()
        qs = Product.objects.filter(id__in=qs_id_list)
        query = self.request.GET.get("keywords", None)
        query_price = self.request.GET.get("price", None)
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(title__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        context['carts'] = global_cart_detail(self.request)
        context['max_price'] = ProductListView.get_max_price()
        return context
