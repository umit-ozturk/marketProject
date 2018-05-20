from django.conf import settings
from django.urls import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


def upload_location(instance, filename):
	upload_path = "img/product/" + str(instance) + "\_" + str(filename)
	return upload_path

class Product(models.Model):
	category 		= TreeForeignKey("categories.category", on_delete=models.CASCADE, null=True,blank=True)
	company 		= models.ForeignKey("companies.company", on_delete=models.CASCADE, related_name="company")
	name 			= models.CharField(max_length=140)
	title 			= models.CharField(max_length=140)
	price 			= models.DecimalField(max_digits=6, decimal_places=2)
	exist 			= models.BooleanField(verbose_name='Stockta Var Mı?', default=True)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	image_prod		= models.ImageField(upload_to=upload_location,
					 		null=True,
							width_field="width_field", 
			 				height_field="height_field")
	height_field	= models.IntegerField(default=0, blank=True)
	width_field 	= models.IntegerField(default=0, blank=True)

	def get_absolute_url(self):
		return reverse("product:detail", kwargs={'pk':self.pk})


	def __str__(self):
		return str(self.pk) + "\t" + str(self.title) 