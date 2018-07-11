from django.contrib import admin
# Register your models here.
from django.template.defaultfilters import truncatechars
from .models import Product



class ProductAdmin(admin.ModelAdmin):
	list_display = ('show_name', 'show_title', 'price', 'company', 'category', 'image_tag', )
	list_filter = ('company', 'category')
	search_fields = ('name', 'title', 'price', )

	def show_title(self, obj): # Product Explanation for Admin Panel
		return truncatechars(obj.title, 35)
	show_title.short_description = 'Ürün Açıklaması'

	def show_name(self, obj): # Product Name for Admin Panel
		return truncatechars(obj.name, 20)
	show_name.short_description = 'Ürün Adı'		

admin.site.register(Product, ProductAdmin)