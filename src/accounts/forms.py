from django import forms
from django.contrib.auth import get_user_model

from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset, Field, HTML, Button

from .models import UserProfile


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
		self.helper.attrs = {'novalidate': ''}
		self.helper.layout = Layout(
			Div(
				HTML(
						"<label>* Kullanıcı Adı</label>"
						
					),				

				Div(
					HTML(
						"<span class='input-group-addon'><i class='fa fa-user'></i></span>"
						), 					
					Field('username', style="width: 100%;", ), css_class='col-md-12 input-group'
					), css_class='form-group col-lg-10'
				),
			Div(
				HTML(
						"<label>* Parola</label>"
						
					),				

				Div(
					HTML(
						"<span class='input-group-addon'><i class='fa fa-user'></i></span>"
						), 					
					Field('password', style="width: 100%;", ), css_class='col-md-12 input-group'
					), css_class='form-group col-lg-6'
				),
			Div(
				HTML(
						"<label>* Tekrar Parola</label>"
						
					),				

				Div(
					HTML(
						"<span class='input-group-addon'><i class='fa fa-user'></i></span>"

						), 					
					Field('password2', style="width: 100%;", ), css_class='col-md-12 input-group'
					), css_class='form-group col-lg-6'
				),
			Div(
				HTML(
						"<label>* E-Mail</label>"
						
					),				

				Div(
					HTML(
						"<span class='input-group-addon'><i class='fa fa-user'></i></span>"
						), 					
					Field('email', style="width: 100%;", ), css_class='col-md-12 input-group'
					), css_class='form-group col-lg-6'
				),
			Div(
				HTML(
						"<label>* Tekrar E-Mail</label>"
						
					),	

				Div(
					HTML(
						"<span class='input-group-addon'><i class='fa fa-user'></i></span>"
						), 					
					Field('email2', style="width: 100%;", ), css_class='col-md-12 input-group'
					), css_class='form-group col-lg-6'
				),
			Div(
				Div(
					Field('info',
						HTML(
							"<div class='form-group'><div class='checkbox checbox-switch switch-danger'><label><input type='checkbox' name='info' checked='' /><span></span>Bilgilendirmelerden beni haberdar et.</label></div></div>",
							), style=""
						), css_class='col-md-12 input-group'
					), css_class='form-group col-lg-6'
				),			
			Div(
				HTML(
						"<button type='submit'>Submit</button>"
						
					), css_class='form-group col-lg-6'
				),			
																			
			)
	def clean(self):
		cleaned_data = super(UserRegisterForm, self).clean()
		email = cleaned_data.get("email")
		email2 = cleaned_data.get("email2")
		password = cleaned_data.get("password")
		password2 = cleaned_data.get("password2")
		username = cleaned_data.get("username")
		if not password and not password2 or password != password2:
			raise forms.ValidationError('* Parolalar eşleşmiyor.')
		if not email and not email2 or email != email2:
			raise forms.ValidationError('* Mail adresleri eşleşmiyor.')
		if User.objects.filter(email=email):
			raise forms.ValidationError('* Mail adresi bu sitede zaten mevcut.')
		if User.objects.filter(username=username):
			raise forms.ValidationError('* Kullanıcı adı bu sitede zaten mevcut.')
		return self.cleaned_data







class UserUpdateForm(forms.ModelForm):
	userphoto 	= forms.ImageField(label='Profil Fotoğrafı', required = False)

	class Meta:
		model = User
		fields = ['email', 'username', 'userphoto', ]


	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'user-update-form'
		self.helper.form_show_labels = False
		self.helper.attrs = {'novalidate': ''}
		self.helper.layout = Layout(
			Div(
				Div(
					HTML(
						"<img alt='User Pic' src='{{user.userphoto}}' class='img-circle img-responsive'>"
						), 					
					Field('userphoto', ), css_class='col-md-3 col-lg-3'
					),

				Div(
					HTML(
						"<table class='table table-user-information'><tbody><tr><td>İsim:</td><td><input type='text' name='lname' placeholder='{{user.name}}'></td></tr><tr><td>Soyisim:</td><td><input type='text' name='lname' placeholder='{{user.surname}}'></td></tr><tr><td>Doğum Tarihi:</td><td><input type='text' name='lname' placeholder='{{user.birthday}}'></td></tr><tr><tr><td>Cinsiyet:</td><td><input type='text' name='lname' placeholder='{{user.gender}}'></td></tr><tr><td>Adres:</td><td><input type='text' name='lname' placeholder='{{user.adress}}'></td></tr><tr><td>Email:</td><td><input type='text' name='lname' placeholder='{{user.email}}'></td></tr><td>Telefon Numarası:</td><td><input type='text' name='lname' placeholder='{{user.phone}}'></td></tr></tbody></table><a href='' type='submit' class='btn btn-fill'>Kaydet</a><button type='submit'>Submit</button><a href='' class='btn btn-primary'>Geri Dön</a>"
						), css_class='col-md-9 col-lg-9'
					), css_class='form-group col-lg-10'
				),				
																			
			)









