from django.contrib.auth import get_user_model, login, authenticate
from django.views.generic.edit import FormView

from django.views.generic  import (
			DetailView
			)

from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegisterForm
from .models import UserProfile


User = get_user_model()


class UserRegisterView(FormView):
	model = UserProfile
	template_name = "accounts/user_register_form.html"
	form_class = UserRegisterForm

	def get_success_url(self):
		return reverse_lazy("home")

	def form_valid(self, form):
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create(username=username, email=email)
		new_user.set_password(password)
		new_user.save()
		user = authenticate(username=username, password=password)
		login(self.request, user)		
		return super(UserRegisterView, self).form_valid(form)

class UserDetailView(DetailView):
	model = UserProfile
	template_name = 'accounts/user_detail.html'
	queryset = User.objects.all()
	
	def get_slug_field(self):
		"""Get the name of a slug field to be used to look up by slug."""
		print(self.model.user)
		return "username"


	def get_context_data(self, *args, **kwargs):
		context = super(UserDetailView, self).get_context_data(*args, **kwargs)
		return context



#class ProfileDetailView(DetailView):
#	model = UserProfile
#	template_name = "accounts/user_profile.html"
#
#	def get_slug_field(self):
#		"""Get the name of a slug field to be used to look up by slug."""
#		print(self.model.user)
#		return 'user__username'



#class UserRegisterView(FormView):
	#template_name = "accounts/user_register_form.html"
	#form_class = UserRegisterForm
	#success_url = "/login"

	#def form_valid(self, form):
	#	username = form.cleaned_data.get("username")
	#	print(username)
	#	email = form.cleaned_data.get("email")
	#	print(email)
	#	password = form.cleaned_data.get("password")
	#	print(password)
	#	new_user = UserProfile.objects.create(username=username, email=email)
	#	print(new_user)
	#	new_user.set_password(password)
	#	new_user.save()
	#	return super(UserRegisterView, self).form_valid(form)
