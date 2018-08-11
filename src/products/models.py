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

class ProducCompanytManager(models.Manager):
	def get_queryset(self):
		super().get_queryset().filter(company_company_name='Roald Dahl')


class Product(models.Model):
	category 		= TreeForeignKey("categories.category", on_delete=models.CASCADE, 
									null=True,blank=True, verbose_name='Kategori')
	company 		= models.ForeignKey("companies.company", on_delete=models.CASCADE, related_name="company", 
										verbose_name='Firma', null=True,  blank=True)
	name 			= models.CharField(max_length=140, verbose_name='Ürün Adı', null=True,  blank=True)
	title 			= models.CharField(max_length=140, verbose_name='Ürün Başlığı', null=True,  blank=True)
	price 			= models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Fiyat', null=True,  blank=True)
	exist 			= models.BooleanField(verbose_name='Stockta Var Mı?', default=True)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	image_prod		= models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", 
										height_field="height_field", verbose_name='Ürün Resmi')
	content 		= RichTextField(verbose_name='Ürün Açıklaması', null=True, blank=True)
	feature 		= RichTextField(verbose_name='Ürün Özellikleri', null=True, blank=True)
	height_field	= models.IntegerField(default=0, blank=True)
	width_field 	= models.IntegerField(default=0, blank=True)

	objects = models.Manager() 
	objects_company = ProducCompanytManager()

	def get_absolute_url(self):
		return reverse("product:detail", kwargs={'pk':self.pk})

	def get_filters(self):
		filters = self.category.category_name
		return filters

	def image_tag(self):
		if self.image_prod:
			return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_prod.url)
		else:
			return 'No Image Found'
	image_tag.short_description = 'Resim'
