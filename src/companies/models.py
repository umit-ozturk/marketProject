from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


def upload_location(instance, filename):
	upload_path = "img/company/" + str(instance) + "\_" + str(filename)
	return upload_path


class Company(MPTTModel):
	parent				= TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
	company_name 		= models.CharField(max_length=140)
	company_site 		= models.CharField(max_length=140)
	image_comp		 	= models.ImageField(upload_to=upload_location,
					 		null=True, blank=True,
							width_field="width_field", 
			 				height_field="height_field")
	height_field 		= models.IntegerField(default=0)
	width_field 		= models.IntegerField(default=0)
##	acıklama
##	vs.vs 

	def __str__(self):
		return str(self.company_name)