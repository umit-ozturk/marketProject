from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView

from .forms import UserRegisterForm

from django.views.generic  import (
			DetailView
			)


from django.shortcuts import render
from .models import UserProfile



# Create your views here.


User = get_user_model()



class ProfileDetailView(DetailView):
	model = UserProfile
	template_name = "accounts/user_profile.html"

	def get_slug_field(self):
		"""Get the name of a slug field to be used to look up by slug."""
		return 'user__username'



class UserRegisterView(FormView):
	template_name = "accounts/user_register_form.html"
	form_class = UserRegisterForm
	success_url = "/login"

	def form_valid(self, form):
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create(username=username, email=email)
		new_user.set_password(password)
		new_user.save()
		return super(UserRegisterView, self).form_valid(form)
