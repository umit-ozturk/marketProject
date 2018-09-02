from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from mptt.admin import MPTTModelAdmin
from .models import Category
from .resources import CategoryResource
from django.template.defaultfilters import truncatechars
# Register your models here.


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, MPTTModelAdmin):
	resources_class = CategoryResource
	fields = ['category_name', 'category_defination', 'parent', 'category_slug', 'category_logo', 'image_prod']
	list_display = ('category_name', 'show_cat_defination', 'parent', 'image_logo_cat', 'image_cat', 'category_slug', )
	search_fields = ('category_name',)
	mptt_level_indent = 15

	def show_cat_defination(self, obj):
		return truncatechars(obj.category_defination, 20)
	show_cat_defination.short_description = 'Kategori Açıklaması'