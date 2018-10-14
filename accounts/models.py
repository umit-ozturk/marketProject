from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from versatileimagefield.fields import VersatileImageField
from django.utils import translation
from django.contrib.auth.models import AnonymousUser
# Create your models here.

User = get_user_model()


def upload_location(instance, filename):
    upload_path = "img/accounts/" + str(filename)
    return upload_path


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('E', 'Erkek'),
        ('K', 'Kadın'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile',
                                            null=True,  blank=True)
    userphoto = VersatileImageField('Kullanıcı Resmi', upload_to=upload_location, null=True, blank=True,
                                    width_field="width_field",  height_field="height_field")
    name = models.CharField('İsim', max_length=50, null=True, blank=True)
    surname = models.CharField('Soyisim', max_length=50, null=True, blank=True)
    birthday = models.DateField('Doğum Tarihi', blank=True, null=True)
    gender = models.CharField('Cinsiyet', max_length=1, choices=GENDER_CHOICES, default='E')
    adress = models.CharField('Adres', max_length=200, blank=True, null=True)
    phone = models.CharField('Telefon Numarası', max_length=15, blank=True, null=True)
    height_field = models.PositiveIntegerField('Uzunluk Değeri', default=0, blank=True)
    width_field = models.PositiveIntegerField('Genişlik Değeri', default=0, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.user.username)

    @classmethod
    def for_request(cls, request):
        user = getattr(request, "user", None)
        if user and user.is_authenticated():
            try:
                return UserProfile._default_manager.get(user=user)
            except UserProfile.DoesNotExist:
                pass
        return AnonymousAccount(request)

    def gender_verbose(self):
        return dict(UserProfile.GENDER_CHOICES)[self.gender]

    def get_slug_field(self):
        """Get the name of a slug field to be used to look up by slug."""
        return "user__username"

    def get_absolute_url(self):
        return reverse_lazy("profile:detail", kwargs={"username":self.user.username})

    @staticmethod
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
    instance.profile.save()
    # celery + redis


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
