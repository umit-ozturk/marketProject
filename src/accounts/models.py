from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse_lazy
# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

	@classmethod
	def for_request(cls, request):
		user = getattr(request, "user", None)
		if user and is_authenticated(user):
			try:
				return UserProfile._default_manager.get(user=user)
			except UserProfile.DoesNotExist:
				pass
		return AnonymousAccount(request)	

	def __str__(self):
		return str(self.user.username)

	def get_absolute_url(self):
		return reverse_lazy("profile:detail", kwargs={"username":self.user.username})

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		new_profile = UserProfile.objects.get_or_create(user=instance)
		#celery + redis


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save(sender, **kwargs):
	if kwargs.get("raw", False):
		return False

	user, created = kwargs["instance"], kwargs["created"]
	disabled = getattr(user, "_disable_account_creation", not settings.ACCOUNT_CREATE_ON_SAVE)
	if created and not disabled:
		UserProfile.create(user=user)



class AnonymousAccount(object):

	def __init__(self, request=None):
		self.user = AnonymousUser()
		self.timezone = settings.TIME_ZONE
		if request is None:
			self.language = settings.LANGUAGE_CODE
		else:
			self.language = translation.get_language_from_request(request, check_path=True)

	def __str__(self):
		return "AnonymousAccount"		