from django.db import models


class Extra_Footer_Contact(models.Model):
	footer_head			= models.CharField('Footer İletişim Bilgisi', max_length=280, null=True,  blank=True)
	icon				= models.CharField('Footer İletişim İconu', max_length=280, null=True,  blank=True)
	link 				= models.CharField('Footer İletişim Linki', max_length=280, null=True,  blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Footer Bilgi'
		verbose_name_plural = 'Footer Bilgileri'
		ordering = ('-created_at',)


class Extra_Footer_Head_1(models.Model):
	text			= models.CharField('Footer Üst 1. Kısım Bilgisi', max_length=280, null=True,  blank=True)
	icon				= models.CharField('Footer Üst 1. Kısım İconu', max_length=280, null=True,  blank=True)
	link 				= models.CharField('Footer Üst 1. Kısım Linki', max_length=280, null=True,  blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Footer Üst 1. Kısım Bilgisi'
		verbose_name_plural = 'Footer Üst 1. Kısım Bilgileri'
		ordering = ('-created_at',)


class Extra_Footer_Head_2(models.Model):
	text			= models.CharField('Footer Üst 2. Kısım Bilgisi', max_length=280, null=True,  blank=True)
	icon				= models.CharField('Footer Üst 2. Kısım İconu', max_length=280, null=True,  blank=True)
	link 				= models.CharField('Footer Üst 2. Kısım Linki', max_length=280, null=True,  blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Footer Üst 2. Kısım Bilgisi'
		verbose_name_plural = 'Footer Üst 2. Kısım Bilgileri'
		ordering = ('-created_at',)


class Extra_Footer_Head_3(models.Model):
	text			= models.CharField('Footer Üst 3. Kısım Bilgisi', max_length=280, null=True,  blank=True)
	icon				= models.CharField('Footer Üst 3. Kısım İconu', max_length=280, null=True,  blank=True)
	link 				= models.CharField('Footer Üst 3. Kısım Linki', max_length=280, null=True,  blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Footer Üst 3. Kısım Bilgisi'
		verbose_name_plural = 'Footer Üst 3. Kısım Bilgileri'
		ordering = ('-created_at',)


class Extra_Footer_Bottom_1(models.Model):
	text			= models.CharField('Footer Alt 1. Kısım Bilgisi', max_length=280, null=True,  blank=True)
	icon				= models.CharField('Footer Alt 1. Kısım İconu', max_length=280, null=True,  blank=True)
	link 				= models.CharField('Footer Alt 1. Kısım Linki', max_length=280, null=True,  blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Footer Alt 1. Kısım Bilgisi'
		verbose_name_plural = 'Footer Alt 1. Kısım Bilgileri'
		ordering = ('-created_at',)


class Extra_Footer_Bottom_2(models.Model):
	text			= models.CharField('Footer Alt 2. Kısım Bilgisi', max_length=280, null=True,  blank=True)
	icon				= models.CharField('Footer Alt 2. Kısım İconu', max_length=280, null=True,  blank=True)
	link 				= models.CharField('Footer Alt 2. Kısım Linki', max_length=280, null=True,  blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Footer Alt 2. Kısım Bilgisi'
		verbose_name_plural = 'Footer Alt 2. Kısım Bilgileri'
		ordering = ('-created_at',)


class Extra_Footer_Bottom_3(models.Model):
	text			= models.CharField('Footer Alt 3. Kısım Bilgisi', max_length=280, null=True,  blank=True)
	icon				= models.CharField('Footer Alt 3. Kısım İconu', max_length=280, null=True,  blank=True)
	link 				= models.CharField('Footer Alt 3. Kısım Linki', max_length=280, null=True,  blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Footer Alt 3. Kısım Bilgisi'
		verbose_name_plural = 'Footer Alt 3. Kısım Bilgileri'
		ordering = ('-created_at',)