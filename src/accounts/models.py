from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse_lazy
# Create your models here.


class UserProfileManager(models.Manager):
	use_for_related_fields = True

	def all(self):
		qs = self.get_queryset().all()
		try:
			if self.instance:
				qs = qs.exclude(user=self.instance)
		except:
			pass
		return qs


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

	objects = UserProfileManager()

	def __str__(self):
		return str(self.user.username)

	def get_absolute_url(self):
		return reverse_lazy("profile:detail", kwargs={"username":self.user.username})

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		new_profile = UserProfile.objects.get_or_create(user=instance)
		#celery + redis


post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL) 