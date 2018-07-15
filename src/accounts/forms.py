from django import forms
from django.contrib.auth import get_user_model

from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset, Field, HTML


User = get_user_model()



class UserRegisterForm(forms.Form):

	username 	= forms.CharField(label='Kullanıcı Adı', max_length=100, required = True)
	email 		= forms.CharField(label='Mail Adresi', max_length=100, required = True)
	email2 		= forms.CharField(label='Tekrar Mail Adresi', max_length=100, required = True)
	password 	= forms.CharField(label='Parola',widget=forms.PasswordInput, max_length=100, required = True)
	password2 	= forms.CharField(label='Tekrar Parola', widget=forms.PasswordInput, max_length=100, required = True)
	info 		= forms.BooleanField(label='Bilgilendirmelerden beni haberdar et.', required=False)


	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'user-register-form'
		self.helper.form_action = reverse('register')
		self.helper.form_show_labels = False
		self.helper.layout = Layout(
			Div(
				HTML(
						"<label>Kullanıcı Adı</label>"
						
					),				

				Div(
					HTML(
						"<span class='input-group-addon'><i class='fa fa-user'></i></span>"
						), 					
					Field('username', style="width: 100%;", ), css_class='col-md-12 input-group'
					), css_class='form-group col-lg-10'
				),
			)
