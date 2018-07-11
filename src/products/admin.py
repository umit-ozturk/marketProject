from django.contrib import admin
# Register your models here.

from .models import Product



class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'title', 'price', 'company', 'category', 'image_tag', )
	list_filter = ('company', 'category')
	search_fields = ('name', 'title', 'price', )

admin.site.register(Product, ProductAdmin)