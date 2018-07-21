from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import TreeForeignKey
from django.template.defaultfilters import truncatechars
from ckeditor.fields import RichTextField

# Create your models here.


def upload_location(instance, filename):
	upload_path = "img/product/" + str(filename)
	return upload_path

#product.category.CATEGORY.category_name

class Product(models.Model):
	category 		= TreeForeignKey("categories.category", on_delete=models.CASCADE, null=True,blank=True, verbose_name='Kategori')
	company 		= models.ForeignKey("companies.company", on_delete=models.CASCADE, related_name="company", verbose_name='Firma')
	name 			= models.CharField(max_length=140, verbose_name='Ürün Adı')
	title 			= models.CharField(max_length=140, verbose_name='Ürün Başlığı', blank=True) # Product Explanation
	price 			= models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Fiyat')
	exist 			= models.BooleanField(verbose_name='Stockta Var Mı?', default=True)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	image_prod		= models.ImageField(upload_to=upload_location,
					 		null=True,
							width_field="width_field", 
			 				height_field="height_field", verbose_name='Ürün Resmi')
	content 		= RichTextField(verbose_name='Ürün Açıklaması')
	height_field	= models.IntegerField(default=0, blank=True)
	width_field 	= models.IntegerField(default=0, blank=True)

	def get_absolute_url(self):
		return reverse("product:detail", kwargs={'pk':self.pk})


	def image_tag(self):
		if self.image_prod:
			return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_prod.url)
		else:
			return 'No Image Found'
	image_tag.short_description = 'Resim'		
