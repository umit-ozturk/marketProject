from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.safestring import mark_safe
# Create your models here.


def upload_location(instance, filename):
	upload_path = "img/company/" + str(instance) + "\_" + str(filename)
	return upload_path


class Company(MPTTModel):
	parent				= TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, 
										related_name='children', db_index=True, verbose_name='Üst Kategori')
	company_name 		= models.CharField(max_length=140, verbose_name='Firma İsmi', null=True,  blank=True)
	company_site 		= models.CharField(max_length=140, verbose_name='Firmanın Sitesi', null=True,  blank=True)
	image_comp		 	= models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", 
			 				height_field="height_field", verbose_name="Firma Resmi")
	height_field 		= models.IntegerField(default=0)
	width_field 		= models.IntegerField(default=0)
##	acıklama
##	vs.vs 

	def __str__(self):
		return str(self.company_name)

	def image_tag(self):
		if self.image_comp:
			return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_comp.url)
		else:
			return 'Resim Bulunamadı'
	image_tag.short_description = 'Resim'		



class Brand(models.Model):
	brand_name = models.CharField(max_length=140, verbose_name='Firma İsmi', null=True,  blank=True)