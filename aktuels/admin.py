from django.contrib import admin
from .models import (
	Aktuel,
	AktuelProducts,
	AktuelSlug
	)
from django.template.defaultfilters import truncatechars


class AktuelAdmin(admin.ModelAdmin):
	list_display = ('slug', 'image_akt', 'image_akt_comp', )
	autocomplete_fields = ['slug',]
	search_fields = ('slug',)


class AktuelSlugAdmin(admin.ModelAdmin):
	list_display = ('title', 'explain', 'aktuel_company_name', 'aktuel_company_site', )
	search_fields = ('slug',)


class AktuelProductsAdmin(admin.ModelAdmin):
	list_display = ('image_akt_prod', 'get_created_at')
	search_fields = ()


admin.site.register(Aktuel, AktuelAdmin)
admin.site.register(AktuelProducts, AktuelProductsAdmin)
admin.site.register(AktuelSlug, AktuelSlugAdmin)
