from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Company

# Register your models here.

class CompanyAdmin(MPTTModelAdmin):
	fields = ['company_name', 'company_site', 'parent']
	list_display = ('company_name', )
	mptt_level_indent = 15

admin.site.register(Company , CompanyAdmin)