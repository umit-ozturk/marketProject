from django.views.generic  import (
            ListView
            )
from .models import AktuelProducts
from cart.views import global_cart_detail


class AktuelProductsListView(ListView):
    queryset = AktuelProducts.objects.all()
    template_name = "aktuels/aktuel_products_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = AktuelProducts.objects.all()
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(AktuelProductsListView, self).get_context_data(*args, **kwargs)
        context['carts'] = global_cart_detail(self.request)
        return context
