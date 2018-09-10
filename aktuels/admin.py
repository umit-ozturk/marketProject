from django.contrib import admin
# Register your models here.
from django.template.defaultfilters import truncatechars
from .models import (
	Aktuel,
	AktuelProducts,
	AktuelSlug
	)


class AktuelAdmin(admin.ModelAdmin):
	list_display = ('image_akt', 'image_akt_comp', 'slug', )
	autocomplete_fields = ['slug',]
	search_fields = ('slug',)

class AktuelSlugAdmin(admin.ModelAdmin):
	list_display = ('title', 'explain', 'aktuel_company_name', 'aktuel_company_site', )
	search_fields = ('slug',)


admin.site.register(Aktuel, AktuelAdmin)
admin.site.register(AktuelSlug, AktuelSlugAdmin)
