from import_export import resources
from .models import Category
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field


class CategoryResource(resources.ModelResource):
	disks = Field(column_name='Disks')
	filesystems = Field(column_name='Filesystems')

	class Meta:
		model = Category
		exclude = []
#
#	def import_field(self, field, obj, data):
#		field_name = self.get_field_name(field)
#		method = getattr(self, 'clean_%s' % field_name, None)
#		if method is not None:
#			obj = method(field, obj, data)
#
#		super(CategoryResource, self).import_field(field, obj, data)
#
#
#	def clean_disks(self, field, obj, data):
#		disks = []
#		cell = data[field.column_name]
#		for e in cell.split(','):
#			e = e.strip().split('-')
#			if len(e) < 3:
#				continue
#			size, disk_type, quality = e
#			qualityi, created = StorageQuality.objects.get_or_create(quality=quality)
#			diski, created = Disk.objects.get_or_create(size=size, disk_type=disk_type, quality=qualityi)
#			disks.append(diski)
#		obj.disks = disks
#		return obj
#
#	def clean_filesystems(self, field, obj, data):
#		filesystems = []
#		cell = data[field.column_name]
#		for e in cell.split(','):
#			e = e.strip().split('-')
#			if len(e) < 3:
#				continue
#			mount, size, quality = e
#			qualityi, created = StorageQuality.objects.get_or_create(quality=quality)
#			filesystemi, created = Filesystem.objects.get_or_create(mount=mount, size=size, quality=qualityi)
#			filesystems.append(filesystemi)
#		obj.filesystems = filesystems
#		return obj