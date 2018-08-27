from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify

# Create your models here.


def upload_location(instance, filename):
	upload_path = "img/aktuel/" + str(filename)
	return upload_path


class Aktuel(models.Model):
	slug 					= models.SlugField('Aktuel Slug', blank=True, unique=True)
	title 					= models.CharField('Aktuel Başlığı', max_length=140, null=True,  blank=True)
	explain					= models.CharField('Aktuel Açıklaması', max_length=140, null=True,  blank=True)
	aktuel_company_name 	= models.CharField('Aktuel Firma Ismi', max_length=140, null=True, blank=True)
	aktuel_company_site 	= models.CharField('Aktuel Firma Sitesi', max_length=140, null=True, blank=True)
	image_aktuel			= models.ImageField('Aktuel Firma Resmi', upload_to=upload_location, null=True, blank=True, 
												width_field="width_field", height_field="height_field")	
	image_comp			 	= models.ImageField('Aktuel Resmi', upload_to=upload_location, null=True, blank=True,
												width_field="width_field", height_field="height_field")
	height_field 			= models.IntegerField('Uzunluk Değeri', default=0, blank=True)
	width_field 			= models.IntegerField('Genişlik Değeri', default=0, blank=True)
	created_at				= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at				= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

	class Meta:
		verbose_name = 'Aktuel'
		verbose_name_plural = 'Aktueller'
		ordering = ('-created_at',)

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

