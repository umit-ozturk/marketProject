from django.db.models import Q
from django.views.generic import (
            DetailView,
            ListView,
            TemplateView
            )
from .models import Product
from categories.models import Category
from cart.views import global_cart_detail
from tickets.views import global_ticket_detail
from django.db.models import Min, Max
from django.http import HttpResponse, Http404
import json

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


class SearchView(TemplateView):
    template_name = 'products/search_product_list.html'
    tab_class = 'search'
    model = Product

    partial_templates = {
        'querys': 'products/search/query.html',
        'values': 'products/search/values.html',
        'pagination': 'products/search/pagination.html'
    }

    method_mapping = {'querys': "get_queries",
                      'prices': "get_values",
                      'paginations': "get_pagination"}

    def dispatch(self, request, *args, **kwargs):
        self.type = request.GET.get('type', 'querys')
        if not self.method_mapping.get(self.type):
            raise Http404()
        return super(SearchView, self).dispatch(request, *args, **kwargs)

    def get_keywords(self):
        return self.request.GET.get('keywords') or ''

    def get_search_bundle(self):
        method = getattr(self, self.method_mapping[self.type])
        return [{'template': self.partial_templates[self.type],
                 'object': item} for item in method()]

    def get_category_count(self):
        return None

    def get_category_detail(self):
        return None

    def get_context_data(self, **kwargs):
        return super(SearchView, self).get_context_data(min_price=self.get_min_price(), max_price=self.get_max_price(),
                                                        category_count=self.get_category_count(),
                                                        category_detail=self.get_category_detail(),
                                                        results=self.get_search_bundle(), **kwargs)


    def get_next_page_url(self):
        return '?keywords=%(keywords)s&price=%(price)s&pagination=%(pagination)s' % {
            "keywords": self.get_queries(),
            "price": self.get_values(),
            "pagination": self.get_pagination()
        }

    def get_queries(self):
        keywords = self.request.GET.get('keywords')
        price = self.request.GET.get('price')
        print(keywords)
        print(price)
        min_value, max_value = self.get_values()
        print(min_value)
        print(max_value)
        if not keywords or len(keywords) < 1:
            result = Product.objects.none()
        else:
            result = (Product.objects.filter(name__icontains=keywords, price__range=(min_value, max_value)))
        return result

    def get_values(self):
        price = self.request.GET.get('price')
        if not price or len(price) < 1:
            return self.get_min_price(), self.get_max_price()
        query_arg = price.split("TL-")
        min_value = price.split("TL-")[0]
        max_value = query_arg[1].split("TL")[0]
        return min_value, max_value

    def get_pagination(self):
        pagination = self.request.GET.get('keywords')
        if not pagination or len(pagination) < 1:
            result = Product.objects.none()
        else:
            result = (Product.objects.filter(title__icontains=pagination,))
        return result

    @staticmethod
    def get_min_price():
        price__min = round(Product.objects.aggregate(Max('price'))['price__max'])
        return price__min

    @staticmethod
    def get_max_price():
        price__max = round(Product.objects.aggregate(Max('price'))['price__max'])
        return price__max


