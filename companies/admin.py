from django.contrib import admin
from .models import Company, Brand

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
	fields = ['company_name', 'company_site', 'image_comp']
	list_display = ('company_name', 'parent', 'company_site', 'image_tag', )
	search_fields = ('company_name',)
	mptt_level_indent = 15


class BrandAdmin(admin.ModelAdmin):
	fields = ['brand_name', 'brand_site', 'brand_description', 'brand_image']
	list_display = ('brand_name', 'brand_site', 'brand_description', )
	search_fields = ('brand_name',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Brand, BrandAdmin)

