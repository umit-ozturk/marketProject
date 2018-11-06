from django.urls import reverse
from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import TreeForeignKey
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField
import os
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

# Create your models here.


def upload_location(instance, filename):
    upload_path = "img/product/" + str(filename)
    return upload_path


class Product(models.Model):
    slug = models.ForeignKey("products.productinfo", verbose_name='Ürün Slug / Sayacı', on_delete=models.CASCADE,
                             related_name="productinfo", null=False,  blank=False)
    category = TreeForeignKey("categories.category", verbose_name='Kategori', on_delete=models.CASCADE,
                              null=False, blank=False)
    company = models.ForeignKey("companies.company", verbose_name='Firma', on_delete=models.CASCADE,
                                related_name="company", null=False,  blank=False)
    brand = models.ForeignKey("companies.brand", verbose_name='Marka', on_delete=models.CASCADE,
                              related_name="brand", null=False,  blank=False)
    name = models.CharField('Ürün Adı', max_length=140, null=True,  blank=True)
    title = models.CharField('Ürün Başlığı', max_length=140, null=True,  blank=True)
    price = models.DecimalField('Ürün Fiyatı', max_digits=6, decimal_places=2, null=True,  blank=True)
    old_price = models.DecimalField('Eski Ürün Fiyatı', max_digits=6, decimal_places=2, null=True,  blank=True)
    content = RichTextField('Ürün Açıklaması', null=True, blank=True)
    feature = RichTextField('Ürün Özellikleri', null=True, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("product:detail", kwargs={'pk': self.pk})

    def get_sale_percent(self):
        if self.old_price is not None or self.price is not None:
            sale_percent = int((self.old_price - self.price) / self.old_price * 100)
        else:
            sale_percent = 0
        return sale_percent

    def get_category_count(self):
        category_count = Product.objects.filter(category_id=self.category.id).count()
        return category_count

    def get_category_detail(self):
        category_detail = Product.objects.filter(category_id=self.category.id)[0]
        return category_detail

    def get_filters(self):
        filters = self.category.category_name
        return filters

    def image_tag(self):
        if self.slug.image_prod_first:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.slug.image_prod_first.url)
        else:
            return 'Resim Bulunamadı.'
    image_tag.short_description = 'Resim'


class ProductInfo(models.Model):
    slug = models.CharField('Ürün Slug / Sayacı', max_length=140, null=True, blank=True)
    image_prod_first = VersatileImageField('Ürün Resmi 1', upload_to=upload_location, null=True, blank=True,
                                         width_field="width_field", height_field="height_field")
    image_prod_second = VersatileImageField('Ürün Resmi 2', upload_to=upload_location, null=True, blank=True,
                                          width_field="width_field", height_field="height_field")
    image_prod_third = VersatileImageField('Ürün Resmi 3', upload_to=upload_location, null=True, blank=True,
                                         width_field="width_field", height_field="height_field")
    image_prod_fourth = VersatileImageField('Ürün Resmi 4', upload_to=upload_location, null=True, blank=True,
                                          width_field="width_field", height_field="height_field")
    height_field = models.PositiveIntegerField('Uzunluk Değeri', default=0, blank=True)
    width_field = models.PositiveIntegerField('Genişlik Değeri', default=0, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Ürün Bilgisi'
        verbose_name_plural = 'Ürün Bilgileri'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.slug)

    def get_slug_count(self):
        slug_count = Product.objects.filter(slug__slug__icontains=self.slug).count()
        return slug_count

    def get_slug_detail(self):
        slug_company_detail = Product.objects.filter(slug__slug__icontains=self.slug)
        return slug_company_detail

    def image_tag(self):
        if self.image_prod_first:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image_prod_first.url)
        else:
            return 'Resim Bulunamadı.'
    image_tag.short_description = 'Resim'


def _delete_file(path):
    # Deletes file from filesystem.
    if os.path.isfile(path):
        os.remove(path)


@receiver(post_delete, sender=ProductInfo)
def delete_img_pre_delete_post(sender, instance, *args, **kwargs):
    if instance:
        try:
            _delete_file(instance.image_prod_first.path)
            _delete_file(instance.image_prod_second.path)
            _delete_file(instance.image_prod_third.path)
            _delete_file(instance.image_prod_fourth.path)
            instance.image_prod_first.delete_sized_images()
            instance.image_prod_second.delete_sized_images()
            instance.image_prod_third.delete_sized_images()
            instance.image_prod_fourth.delete_sized_images()
        except Exception as ex:
            print(ex)
