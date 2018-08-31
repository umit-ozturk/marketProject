from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.safestring import mark_safe
from versatileimagefield.fields import VersatileImageField

# Create your models here.

def upload_location(instance, filename):
	upload_path = "img/category/" + str(filename)
	return upload_path

class Category(MPTTModel):
	parent				= TreeForeignKey('self', verbose_name='Üst Kategori', on_delete=models.CASCADE, null=True, 
										blank=True, related_name='children', db_index=True)
	category_name		= models.CharField('Kategori Ismi',max_length=30, null=True,  blank=True)	
	category_defination = models.CharField('Kategori Açıklaması', max_length=140, null=True,  blank=True)
	category_logo		= models.CharField('Kategori Logo', max_length=50, null=True,  blank=True)
	category_slug		= models.SlugField('Slug', null=True,  blank=True)
	image_prod			= VersatileImageField('Kategori Resmi', upload_to=upload_location, null=True,  blank=True,
											width_field="width_field", height_field="height_field")
	height_field 		= models.PositiveIntegerField('Uzunluk Değeri', default=0, blank=True)
	width_field 		= models.PositiveIntegerField('Genişlik Değeri', default=0, blank=True)
	created_at			= models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
	updated_at			= models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)
	
	class Meta:
		unique_together = (('parent', 'category_slug',))
		verbose_name = 'Kategori'
		verbose_name_plural = 'Kategoriler'
		ordering = ('-created_at',)		

	class MPTTMeta:
		order_insertion_by = ['category_name']	

	def __str__(self):
		return str(self.category_name)

	def root_node(self):
		the_parent = self.tree_id
		return the_parent

	def get_parent(self):
		the_parent = self
		if self.parent:
			the_parent = self.parent
		return the_parent

	def get_children(self):
		parent = self.get_parent()
		qs = Category.objects.filter(parent=parent)
		qs_parent = Category.objects.filter(pk=parent.pk)
		return ( qs | qs_parent )

	def image_cat(self):
		if self.image_prod:
			return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_prod.url)
		else:
			return 'Kategori Resmi Bulunamadı'
	image_cat.short_description = 'Kategori Resmi'

	def image_logo_cat(self):
		flat = 'fa flaticon-'
		if self.category_logo:
			print(mark_safe("<i class='fa flaticon-%s></i>" % self.category_logo))
			return mark_safe('<i class="%s%s"></i>' % (flat, self.category_logo))
		else:
			return 'Kategori Logosu Bulunamadı'
	image_logo_cat.short_description = 'Kategori Logosu'		
