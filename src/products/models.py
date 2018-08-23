from django.urls import reverse
from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import TreeForeignKey
from ckeditor.fields import RichTextField

# Create your models here.


def upload_location(instance, filename):
    upload_path = "img/product/" + str(filename)
    return upload_path


class Product(models.Model):
    slug = models.ForeignKey("products.productinfo", verbose_name='Ürün Slug / Sayacı', on_delete=models.CASCADE,
                             related_name="productinfo", null=True,  blank=True)
    category = TreeForeignKey("categories.category", verbose_name='Kategori', on_delete=models.CASCADE,
                              null=True, blank=True)
    company = models.ForeignKey("companies.company", verbose_name='Firma', on_delete=models.CASCADE,
                                related_name="company", null=True,  blank=True)
    brand = models.ForeignKey("companies.brand", verbose_name='Marka', on_delete=models.CASCADE,
                              related_name="brand", null=True,  blank=True)
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
        sale_percent = int((self.old_price - self.price) / self.old_price * 100)
        return sale_percent

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
    image_prod_first = models.ImageField('Ürün Resmi 1', upload_to=upload_location, null=True, blank=True,
                                         width_field="width_field", height_field="height_field")
    image_prod_second = models.ImageField('Ürün Resmi 2', upload_to=upload_location, null=True, blank=True,
                                          width_field="width_field", height_field="height_field")
    image_prod_third = models.ImageField('Ürün Resmi 3', upload_to=upload_location, null=True, blank=True,
                                         width_field="width_field", height_field="height_field")
    image_prod_fourth = models.ImageField('Ürün Resmi 4', upload_to=upload_location, null=True, blank=True,
                                          width_field="width_field", height_field="height_field")
    height_field = models.IntegerField('Uzunluk Değeri', default=0, blank=True)
    width_field = models.IntegerField('Genişlik Değeri', default=0, blank=True)
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
