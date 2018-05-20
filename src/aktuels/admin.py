from django.contrib import admin

# Register your models here.

from .models import (
	Aktuel,
	AktuelProducts
	)


admin.site.register(Aktuel)
admin.site.register(AktuelProducts)