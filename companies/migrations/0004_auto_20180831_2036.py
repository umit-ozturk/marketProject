# Generated by Django 2.0.2 on 2018-08-31 20:36

import companies.models
from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20180812_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='height_field', null=True, upload_to=companies.models.upload_location, verbose_name='Marka Resmi', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='height_field',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Uzunluk Değeri'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='width_field',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Genişlik Değeri'),
        ),
        migrations.AlterField(
            model_name='company',
            name='height_field',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Uzunluk Değeri'),
        ),
        migrations.AlterField(
            model_name='company',
            name='image_comp',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='height_field', null=True, upload_to=companies.models.upload_location, verbose_name='Firma Resmi', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='company',
            name='width_field',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Genişlik Değeri'),
        ),
    ]