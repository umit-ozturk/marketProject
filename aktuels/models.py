from django.db import models
from django.utils.safestring import mark_safe
from versatileimagefield.fields import VersatileImageField
from django.template.defaultfilters import date as _date
# Create your models here.


def upload_location(instance, filename):
    upload_path = "img/aktuel/" + str(filename)
    return upload_path


class Aktuel(models.Model):
    slug = models.ForeignKey("aktuels.aktuelslug", verbose_name='Aktuel Slug', on_delete=models.CASCADE,
                             related_name="aktuelslug", null=False,  blank=False)
    image_aktuel = VersatileImageField('Aktuel Firma Resmi', upload_to=upload_location, null=True, blank=True,
                                       width_field="width_field", height_field="height_field")
    image_aktuel_comp = VersatileImageField('Aktuel Resmi', upload_to=upload_location, null=True, blank=True,
                                     width_field="width_field", height_field="height_field")
    height_field = models.PositiveIntegerField('Uzunluk Değeri', default=0, blank=True)
    width_field = models.PositiveIntegerField('Genişlik Değeri', default=0, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Aktuel'
        verbose_name_plural = 'Aktueller'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.slug)

    def image_akt(self):
        if self.image_aktuel:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_aktuel.url)
        else:
            return 'Resim Bulunamadı'
    image_akt.short_description = 'Aktuel Resmi'

    def image_akt_comp(self):
        if self.image_aktuel_comp:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_aktuel_comp.url)
        else:
            return 'Resim Bulunamadı'
    image_akt_comp.short_description = 'Aktuel Firma Resmi'


class AktuelProducts(models.Model):
    aktuel = models.ForeignKey(Aktuel, on_delete=models.CASCADE, related_name="aktuel_products")
    image_aktuel_prod = VersatileImageField('Aktuel Ürün Resmi', upload_to=upload_location, null=True,
                                            width_field="width_field", height_field="height_field")
    explain = models.CharField("Açıklama", max_length=300, null=True, blank=True)
    height_field = models.PositiveIntegerField(default=0, blank=True)
    width_field = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Aktuel Ürünü'
        verbose_name_plural = 'Aktuel Ürünleri'
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.aktuel.slug)

    def image_akt_prod(self):
        if self.image_aktuel_prod:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_aktuel_prod.url)
        else:
            return 'Resim Bulunamadı'
    image_akt_prod.short_description = 'Aktuel Firma Resmi'

    def get_created_at(self):
        return _date(self.created_at, "d F, Y")
    get_created_at.short_description = 'Aktuel Tarih'


class AktuelSlug(models.Model):
    title = models.CharField('Aktuel Başlığı', max_length=140, null=True,  blank=True)
    explain = models.CharField('Aktuel Açıklaması', max_length=140, null=True,  blank=True)
    aktuel_company_name = models.CharField('Aktuel Firma Ismi', max_length=140, null=True, blank=True)
    aktuel_company_site = models.CharField('Aktuel Firma Sitesi', max_length=140, null=True, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Aktuel Slug'
        verbose_name_plural = 'Aktuel Slugları'
        ordering = ('-created_at',)

    def __str__(self):
        return '{}  /  {}'.format(self.title, self.aktuel_company_name)
