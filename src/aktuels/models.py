from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify

# Create your models here.


def upload_location(instance, filename):
	upload_path = "img/aktuel/" + str(filename)
	return upload_path

class Aktuel(models.Model):
	title 					= models.CharField(max_length=140, null=True,  blank=True)
	explain					= models.CharField(max_length=140, null=True,  blank=True)
	updated 				= models.DateTimeField(auto_now=True, null=True,  blank=True)
	timestamp				= models.DateTimeField(auto_now_add=True, editable=False)
	image_aktuel			= models.ImageField(upload_to=upload_location, null=True, blank=True, 
												width_field="width_field", height_field="height_field")
	aktuel_company_name 	= models.CharField(max_length=140, verbose_name='Aktuel Firma Ismi', null=True,  blank=True)
	aktuel_company_site 	= models.CharField(max_length=140, verbose_name='Aktuel Firma Sitesi', null=True,  blank=True)
	image_comp			 	= models.ImageField(upload_to=upload_location,
					 		null=True, blank=True,
							width_field="width_field", 
			 				height_field="height_field")
	height_field			= models.IntegerField(default=0, null=True,  blank=True)
	width_field			 	= models.IntegerField(default=0, null=True,  blank=True)
	slug 					= models.SlugField(blank=True, unique=True)

	class Meta:
		verbose_name = 'Aktuel'
		verbose_name_plural = 'Aktueller'
		ordering = ('-timestamp',)

	def __str__(self):
		return str(self.title)		

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Aktuel, self).save(*args, **kwargs)

	def image_akt(self):
		if self.image_aktuel:
			return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_aktuel.url)
		else:
			return 'Resim Bulunamadı'
	image_akt.short_description = 'Aktuel Resmi'

	def image_akt_comp(self):
		if self.image_comp:
			return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_comp.url)
		else:
			return 'Resim Bulunamadı'
	image_akt_comp.short_description = 'Aktuel Firma Resmi'			

	def __str__(self):
		return str(self.pk) + "\t" + str(self.title) 

class AktuelProducts(models.Model):
	aktuel 			= models.ForeignKey(Aktuel, on_delete=models.CASCADE, related_name="aktuel_products")
	name 			= models.CharField(max_length=140)
	title 			= models.CharField(max_length=140)
	price 			= models.DecimalField(max_digits=6, decimal_places=2)
	exist 			= models.BooleanField(verbose_name='Stockta Var Mı?', default=True)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp		= models.DateTimeField(auto_now_add=True, editable=False)
	image_prod		= models.ImageField(upload_to=upload_location,
					 		null=True,
							width_field="width_field", 
			 				height_field="height_field")
	height_field	= models.IntegerField(default=0, blank=True)
	width_field 	= models.IntegerField(default=0, blank=True)

	class Meta:
		verbose_name = 'Aktuel Ürünü'
		verbose_name_plural = 'Aktuel Ürünleri'
		ordering = ('-timestamp',)	

	def __str__(self):
		return str(self.name) 


def pre_save_aktuel_create(sender, m, *args, **kwargs):
	slug = slugify(m.title)
	check = Aktuel.objects.filter(slug=slug).exists()
	if check:
		slug = "%s-%s" % (slug, m.id)
	m.slug = slug

#pre_save.connect(pre_save_aktuel_create, sender=Aktuel)

