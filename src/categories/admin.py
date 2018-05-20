from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from mptt.admin import MPTTModelAdmin
from .models import Category
from .resources import CategoryResource
from import_export import resources
# Register your models here.



@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, MPTTModelAdmin):
	resources_class = CategoryResource
	fields = ['category_name', 'category_defination', 'parent', 'category_slug', 'category_logo', 'image_prod']
	list_display = ('category_name', )
	mptt_level_indent = 15

