from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView

from .forms import UserRegisterForm


from .models import UserProfile



# Create your views here.


User = get_user_model()


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
