from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django.template.defaultfilters import truncatechars
from .models import Company, Brand

# Register your models here.

class CompanyAdmin(MPTTModelAdmin):
	fields = ['company_name', 'company_site', 'parent', 'image_comp',]
	list_display = ('company_name', 'parent', 'company_site', 'image_tag', )
	search_fields = ('company_name',)
	mptt_level_indent = 15

class BrandAdmin(admin.ModelAdmin):
	fields = ['brand_name', 'brand_site', 'brand_description', 'brand_image',]
	list_display = ('brand_name', 'brand_site', 'brand_description', )
	search_fields = ('brand_name',)

admin.site.register(Company , CompanyAdmin)
admin.site.register(Brand , BrandAdmin)

