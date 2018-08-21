from django.contrib import admin
import json
from django.template.defaultfilters import truncatechars
from .models import Product
from django.conf.urls import url
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseBadRequest


from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from .forms import ProductForm


class ProductAdmin(AjaxSelectAdmin):
	list_display = ('show_name', 'show_title', 'price', 'company', 'category', 'image_tag', )
	list_filter = ('company', 'category')
	search_fields = ('name', 'title', 'price', 'slug',)
	search_prefix = '__icontains'
	autocomplete_fields = ['company', 'brand', 'category']
	change_list_template = 'products/change_form.html'
	form = ProductForm

	def get_urls(self):
		urls = super(ProductAdmin, self).get_urls()
		print(urls)
		api_urls = [
			url(r'^search/(?P<search_term>\w{0,50})$', self.search_api)
		]
		return api_urls + urls

	def search_api(self, request, search_term):
		if not self.search_fields:
			return HttpResponseBadRequest(reason='Aramanızla Eşleşen Ürün Yok {}'.format(self.__name__))
		elif not search_term:
			return HttpResponseBadRequest(reason='Bir Sorun Oluştu.')
		else:
			keyword = self.search_fields[3]
			options = {
				keyword + self.search_prefix: search_term,
			}
			data = []

			for instance in self.model.objects.filter(**options):
				data.append(
					{
						'keyword': getattr(instance, keyword),
						'list_url': self.get_change_list_url(self.model, instance, self.model.app_label),
					}
				)

			data = json.dumps(data)

			return HttpResponse(content=data, content_type='application/json')

	@staticmethod
	def get_change_list_url(model, instance, app_label):
		""" /django/contrib/admin/options/get_urls 'i override ediyoz. """
		return reverse(
			"admin:%s_%s_add" % (app_label, str(model.__name__).lower()), args=(instance.id,)
			)

	def show_title(self, obj): # Product Explanation for Admin Panel
		return truncatechars(obj.title, 35)
	show_title.short_description = 'Ürün Başlığı'
	show_title.short_description = 'Ürün Açıklaması'

	def show_name(self, obj): # Product Name for Admin Panel
		return truncatechars(obj.name, 20)
	show_name.short_description = 'Ürün Adı'		


admin.site.register(Product, ProductAdmin)