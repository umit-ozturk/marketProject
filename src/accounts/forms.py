from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegisterForm(forms.Form):
	username = forms.CharField(label="Kullanıcı Adı", required = True)
	email = forms.EmailField(label='Mail Adresi', required = True)
	password = forms.CharField(label='Parola',widget=forms.PasswordInput,required = True)
	password2 = forms.CharField(label='Tekrar Parola', widget=forms.PasswordInput, required = True)



	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")

		if password != password2:
			raise form.ValidationError("Paralolar eşleşmiyor.")
		return password2

	def clean_username(self):
		username = self.cleaned_data.get("username")
		if User.objects.filter(username__icontains=username).exists():
			raise form.ValidationError("Bu kullanıcı adı zaten alınmış.")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if User.objects.filter(email__icontains=email).exists():
			raise form.ValidationError("Bu mail adresi zaten kayıtlı.")
		return email