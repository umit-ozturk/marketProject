from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import Product, ProductInfo


class ProductAdmin(admin.ModelAdmin):
    list_display = ('show_name', 'show_title', 'price', 'company', 'category', 'image_tag',)
    list_filter = ('company', 'category',)
    search_fields = ('title', 'price', 'name', 'slug')
    autocomplete_fields = ['slug', 'category', 'company', 'brand', ]

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
