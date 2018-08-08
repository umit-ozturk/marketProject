from django.contrib import admin
# Register your models here.
from django.template.defaultfilters import truncatechars
from .models import (
	Aktuel,
	AktuelProducts
	)




class AktuelAdmin(admin.ModelAdmin):
	list_display = ('show_title', 'show_explain', 'image_akt', 'aktuel_company_name', 'aktuel_company_site', 'image_akt_comp', 'slug', )
	search_fields = ('aktuel_company_name', 'title', )

	def show_title(self, obj): # Product Explanation for Admin Panel
		return truncatechars(obj.title, 20)
	show_title.short_description = 'Aktuelin Başlığı'

	def show_explain(self, obj): # Product Name for Admin Panel
		return truncatechars(obj.explain, 35)
	show_explain.short_description = 'Aktuelin Açıklaması'		

admin.site.register(Aktuel, AktuelAdmin)