# Generated by Django 2.0.2 on 2018-08-23 14:25

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_old_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=140, null=True, verbose_name='Ürün Slug / Sayacı')),
                ('image_prod_first', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 1', width_field='width_field')),
                ('image_prod_second', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 2', width_field='width_field')),
                ('image_prod_third', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 3', width_field='width_field')),
                ('image_prod_fourth', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, verbose_name='Ürün Resmi 4', width_field='width_field')),
                ('height_field', models.IntegerField(blank=True, default=0, verbose_name='Uzunluk Değeri')),
                ('width_field', models.IntegerField(blank=True, default=0, verbose_name='Genişlik Değeri')),
            ],
            managers=[
                ('objects_company', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_prod_first',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_prod_fourth',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_prod_second',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_prod_third',
        ),
        migrations.RemoveField(
            model_name='product',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productinfo', to='products.ProductInfo', verbose_name='Ürün Bilgisi'),
        ),
    ]