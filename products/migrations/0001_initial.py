# Generated by Django 2.0.2 on 2018-11-24 13:04

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import products.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=140, null=True, verbose_name='Ürün Adı')),
                ('title', models.CharField(blank=True, max_length=140, null=True, verbose_name='Ürün Başlığı')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Ürün Fiyatı')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Eski Ürün Fiyatı')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ürün Açıklaması')),
                ('feature', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ürün Özellikleri')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='companies.Brand', verbose_name='Marka')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category', verbose_name='Kategori')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='companies.Company', verbose_name='Firma')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=140, null=True, verbose_name='Ürün Slug / Sayacı')),
                ('image_prod_first', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 1', width_field='width_field')),
                ('image_prod_second', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 2', width_field='width_field')),
                ('image_prod_third', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 3', width_field='width_field')),
                ('image_prod_fourth', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 4', width_field='width_field')),
                ('height_field', models.PositiveIntegerField(blank=True, default=0, verbose_name='Uzunluk Değeri')),
                ('width_field', models.PositiveIntegerField(blank=True, default=0, verbose_name='Genişlik Değeri')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Ürün Bilgisi',
                'verbose_name_plural': 'Ürün Bilgileri',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productinfo', to='products.ProductInfo', verbose_name='Ürün Slug / Sayacı'),
        ),
    ]
