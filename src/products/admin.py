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
    list_display = ('show_name', 'show_title', 'price', 'company', 'category', )
    list_filter = ('company', 'category')
    search_fields = ('title', 'price', 'name',)
    search_prefix = '__icontains'
    change_list_template = 'products/change_list.html'
    raw_id_fields = ('slug',)

    def get_urls(self):
        urls = super(ProductAdmin, self).get_urls()
        api_urls = [
            url(r'^search/(?P<search_term>\w{0,50})$', self.search_api)
        ]
        return api_urls + urls

    def search_api(self, search_term):
        if not self.search_fields:
            return HttpResponseBadRequest(reason='Mo search_fields defined in {}'.format(self.__name__))
        elif not search_term:
            return HttpResponseBadRequest(reason='Mo search term provided')
        else:
            keyword = self.search_fields[0]
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

    @staticmethod
    def get_change_form_url(model, instance, app_label):
        return reverse(
            "admin:%s_%s_change" % (app_label, str(model.__name__).lower()), args=(instance.id,)
        )

    def show_title(self, obj):  # Product Explanation for Admin Panel
        return truncatechars(obj.title, 35)
    show_title.short_description = 'Ürün Başlığı'
    show_title.short_description = 'Ürün Açıklaması'

    def show_name(self, obj):  # Product Name for Admin Panel
        return truncatechars(obj.name, 20)
    show_name.short_description = 'Ürün Adı'


class ProductInfoAdmin(admin.ModelAdmin):
    fields = ['slug', 'image_prod_first', 'image_prod_second', 'image_prod_third', 'image_prod_fourth', ]
    list_display = ('slug', 'image_prod_first',)
    search_fields = ('slug',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
