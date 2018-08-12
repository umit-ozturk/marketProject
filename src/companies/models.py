from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
# Create your models here.


def upload_location(instance, filename):
	upload_path = "img/company/"+ str(filename)
	return upload_path


class Company(MPTTModel):
	parent				= TreeForeignKey('self', verbose_name='Üst Kategori', on_delete=models.CASCADE, null=True, 
										blank=True, related_name='children', db_index=True)
	company_name 		= models.CharField('Firma İsmi', max_length=140, null=True,  blank=True)
	company_site 		= models.CharField('Firmanın Sitesi', max_length=140, null=True,  blank=True)
	company_description = RichTextField('Firma Açıklaması', null=True, blank=True)
	image_comp		 	= models.ImageField('Firma Resmi', upload_to=upload_location, null=True, blank=True, 
											width_field="width_field", height_field="height_field")
	height_field 		= models.IntegerField('Uzunluk Değeri', default=0, blank=True)
	width_field 		= models.IntegerField('Genişlik Değeri', default=0, blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Firma'
		verbose_name_plural = 'Firmalar'
		ordering = ('-created_at',)	

	def __str__(self):
		return str(self.company_name)

	def image_tag(self):
		if self.image_comp:
			return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_comp.url)
		else:
			return 'Resim Bulunamadı'
	image_tag.short_description = 'Resim'		


class Brand(models.Model):
	brand_name 			= models.CharField('Marka İsmi', max_length=140, null=True,  blank=True)
	brand_site 			= models.CharField('Markanın Sitesi', max_length=140, null=True,  blank=True)
	brand_description	= RichTextField('Marka Açıklaması', null=True, blank=True)	
	brand_image 		= models.ImageField('Marka Resmi', upload_to=upload_location, null=True, blank=True, 
											width_field="width_field", height_field="height_field")
	height_field 		= models.IntegerField('Uzunluk Değeri', default=0, blank=True)
	width_field 		= models.IntegerField('Genişlik Değeri', default=0, blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Marka'
		verbose_name_plural = 'Markalar'
		ordering = ('-created_at',)

	def __str__(self):
		return str(self.brand_name)		