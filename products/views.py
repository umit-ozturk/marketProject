from django.db.models import Q
from django.views.generic import (
            DetailView,
            ListView,
            TemplateView
            )
from .models import Product
from cart.views import global_cart_detail
from tickets.views import global_ticket_detail
from django.db.models import Min, Max
from django.core.paginator import Paginator
from products.mixins import PaginationMixin
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
        print("get_keywords")
        return self.request.GET.get('keywords') or ''

    def is_json(self):
        return (self.request.is_ajax() or
                self.request.GET.get('json'))

    def get_search_bundle(self):
        method = getattr(self, self.method_mapping[self.type])
        return [{'template': self.partial_templates[self.type],
                 'object': item} for item in method()]

    def get_context_data(self, **kwargs):
        return super(SearchView, self).get_context_data(results=self.get_search_bundle(), **kwargs)

    def get_next_page_url(self):
        return '?query=%(query)s&price=%(price)s&pagination=%(pagination)s' % {
            "query": self.get_queries(),
            "price": self.get_values(),
            "pagination": self.get_pagination()
        }

    def get_queries(self):
        keywords = self.request.GET.get('keywords')
        if not keywords or len(keywords) < 2:
            result = Product.objects.none()
        else:
            result = (Product.objects.filter(name__icontains=keywords))
        return result

    def get_values(self):
        print("get_values")
        price = self.request.GET.get('keywords')
        if not price or len(price) < 1:
            result = Product.objects.none()
        else:
            result = (Product.objects.filter(title__icontains=price,))

    def get_pagination(self):
        print("get_pagination")
        pagination = self.request.GET.get('keywords')
        if not pagination or len(pagination) < 2:
            result = Product.objects.none()
        else:
            result = (Product.objects.filter(title__icontains=pagination,))

    def render_to_response(self, context, **response_kwargs):
        if not self.is_json():
            return super(SearchView, self).render_to_response(
                context, **response_kwargs)

        results = [{
                       "id": result['object'].id,
                       "label": result['object']
                   } for result in context['results']]

        return HttpResponse(
            json.dumps(results),
            dict(content_type='application/json', **response_kwargs)
        )

    @staticmethod
    def price_list_min_max():
        price__min = round(Product.objects.aggregate(Min('price'))['price__min'])
        price__max = round(Product.objects.aggregate(Max('price'))['price__max'])
        price_list = {'price__min': price__min, 'price__max': price__max}
        return price_list


#            query_arg = query_price.split("TL-")
#            min_value = query_price.split("TL-")[0]
#            max_value = query_arg[1].split("TL")[0]
#            qs = Product.objects.filter(
#                Q(price__range=(min_value, max_value))
#                ).distinct()
