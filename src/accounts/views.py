from django.contrib.auth import get_user_model, login, authenticate
from django.views.generic.edit import FormView

from django.views.generic  import (
			DetailView,
			UpdateView
			)

from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .forms import (
	UserRegisterForm,
	UserUpdateForm
	)
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



class UserUpdateView(UpdateView):
	model = UserProfile
	template_name = 'accounts/user_update.html'
	form_class = UserUpdateForm

	def form_valid(self, form):
		form.save(commit=False)
		form_data = form.cleaned_data
		for data in form_data:
			if form_data[data] is None or form_data[data] == '':
				form_data[data] = form.initial[data]
				form.instance.__dict__[data] = form.initial[data]
		form.save()
		return super(UserUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy("home")	


	def get_slug_field(self):
		"""Get the name of a slug field to be used to look up by slug."""
		return "user__username"		

class UserDetailView(DetailView):
	model = UserProfile
	template_name = 'accounts/user_detail.html'
	queryset = UserProfile.objects.all()
	
	def get_slug_field(self):
		queryset = User.objects.all()
		"""Get the name of a slug field to be used to look up by slug."""
		return "user__username"


	def get_context_data(self, *args, **kwargs):
		context = super(UserDetailView, self).get_context_data(*args, **kwargs)
		return context

