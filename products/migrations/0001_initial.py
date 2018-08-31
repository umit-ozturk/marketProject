# Generated by Django 2.0.2 on 2018-08-11 18:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import products.models


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
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Fiyat')),
                ('exist', models.BooleanField(default=True, verbose_name='Stockta Var Mı?')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.CharField(blank=True, max_length=140, null=True, verbose_name='Ürün Slug/Sayaç')),
                ('image_prod_first', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 1', width_field='width_field')),
                ('image_prod_second', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 2', width_field='width_field')),
                ('image_prod_third', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 3', width_field='width_field')),
                ('image_prod_fourth', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 4', width_field='width_field')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ürün Açıklaması')),
                ('feature', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ürün Özellikleri')),
                ('height_field', models.IntegerField(blank=True, default=0)),
                ('width_field', models.IntegerField(blank=True, default=0)),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category', verbose_name='Kategori')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='companies.Company', verbose_name='Firma')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
                'ordering': ('-timestamp',),
            },
        ),
    ]