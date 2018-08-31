from django.contrib import admin
from django.contrib.auth import get_user_model
from django.template.defaultfilters import truncatechars
from .models import UserProfile

# Register your models here.

User = get_user_model()

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'show_user', 'show_dummy',)
	search_fields = ('user', )

	def show_dummy(self, obj):
		return obj.user

	def show_user(self, obj): # User Name for Admin Panel
		return truncatechars(obj.user, 20)
	show_user.short_description = 'Kullanıcı Adı'		

admin.site.register(UserProfile, UserProfileAdmin)
