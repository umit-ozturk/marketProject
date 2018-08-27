from django.contrib import admin
import json
from django.template.defaultfilters import truncatechars
from .models import Product, ProductInfo
from django.conf.urls import url
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseBadRequest


class ProductAdmin(admin.ModelAdmin):
    list_display = ('show_name', 'show_title', 'price', 'company', 'category', 'image_tag',)
    list_filter = ('company', 'category',)
    search_fields = ('title', 'slug', 'price', 'name',)
    autocomplete_fields = ['slug', 'category', 'company', 'brand', ]
    search_prefix = '__icontains'
    list_display_list = ('name',)
    change_list_template = 'products/change_list.html'
    change_form_template = 'products/change_form.html'

    def get_urls(self):
        urls = super(ProductAdmin, self).get_urls()
        api_urls = [
            url(r'^search/(?P<search_term>\w{0,50})$', self.search_api_for_list),
            url(r'^search/(?P<search_term>\w{0,50})$', self.search_api_for_add)
        ]
        return api_urls + urls

    def search_api_for_add(self, request, search_term):
        print(self.list_display_list[0])
        if not self.list_display_list[0]:
            return HttpResponseBadRequest(reason='{} Search Fieldi Tanımlanamadı.'.format(self.__name__))
        elif not search_term:
            return HttpResponseBadRequest(reason='Aranan Kelime Desteklenemedi.')
        else:
            keyword = self.list_display_list[0]
            print(keyword)
            options = {
                keyword + self.search_prefix: search_term,
            }
            data = []
            for instance in self.model.objects.filter(**options):
                data.append(
                    {
                        'keyword': getattr(instance, keyword),
                        'url': self.get_change_form_url(self.model, instance, self.model._meta.app_label)
                    }
                )
                data = json.dumps(data)
                return HttpResponse(content=data, content_type='application/json')

    def search_api_for_list(self, request, search_term):
        if not self.search_fields:
            return HttpResponseBadRequest(reason='Mo search_fields defined in {}'.format(self.__name__))
        elif not search_term:
            return HttpResponseBadRequest(reason='Mo search term provided')
        else:
            keyword = self.search_fields[0]
            options = {
                keyword + self.search_prefix: search_term,
            }
            data = []
            for instance in self.model.objects.filter(**options):
                data.append(
                    {
                        'keyword': getattr(instance, keyword),
                        'url': self.get_change_form_url(self.model, instance, self.model._meta.app_label)
                    }
                )
                data = json.dumps(data)
                return HttpResponse(content=data, content_type='application/json')

    @staticmethod
    def get_change_form_url(model, instance, app_label):
        print(model)
        print(instance)
        print(app_label)
        print(instance.__dict__)
        return reverse(
            "admin:products_product_add"
        )

    def show_title(self, obj):  # Product Explanation for Admin Panel
        return truncatechars(obj.title, 35)
    show_title.short_description = 'Ürün Başlığı'

    def show_name(self, obj):  # Product Name for Admin Panel
        return truncatechars(obj.name, 20)
    show_name.short_description = 'Ürün Adı'


class ProductInfoAdmin(admin.ModelAdmin):
    fields = ['slug', 'image_prod_first', 'image_prod_second', 'image_prod_third', 'image_prod_fourth', ]
    list_display = ('slug', 'image_tag',)
    search_fields = ('slug',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
