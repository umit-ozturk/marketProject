from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()



class UserRegisterForm(forms.Form):
	username 	= forms.CharField(label='Kullanıcı Adı', max_length=100, required = True)
	email 		= forms.CharField(label='Mail Adresi', max_length=100, required = True)
	email2 		= forms.CharField(label='Tekrar Mail Adresi', max_length=100, required = True)
	password 	= forms.CharField(label='Parola',widget=forms.PasswordInput, max_length=100, required = True)
	password2 	= forms.CharField(label='Tekrar Parola', widget=forms.PasswordInput, max_length=100, required = True)
	info 		= forms.BooleanField(label='Bilgilendirmelerden beni haberdar et.', required=False)

