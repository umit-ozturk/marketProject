from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

def upload_location(instance, filename):
	upload_path = "img/category/" + str(instance) + "\_" + str(filename)
	return upload_path

class Category(MPTTModel):
	category_name		= models.CharField(max_length=30)
	parent				= TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
	category_defination = models.CharField(max_length=140, blank=True)
	category_logo		= models.CharField(max_length=50)
	category_slug		= models.SlugField()
	image_prod			= models.ImageField(upload_to=upload_location,
					 		null=True,
							width_field="width_field", 
			 				height_field="height_field")
	height_field	= models.IntegerField(default=0, blank=True)
	width_field 	= models.IntegerField(default=0, blank=True)

	class MPTTMeta:
		order_insertion_by = ['category_name']

	class Meta:
		unique_together = (('parent', 'category_slug',))

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