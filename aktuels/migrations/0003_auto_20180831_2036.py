# Generated by Django 2.0.2 on 2018-08-31 20:36

import aktuels.models
from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aktuels', '0002_auto_20180812_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktuel',
            name='height_field',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Uzunluk Değeri'),
        ),
        migrations.AlterField(
            model_name='aktuel',
            name='image_aktuel',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='height_field', null=True, upload_to=aktuels.models.upload_location, verbose_name='Aktuel Firma Resmi', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='aktuel',
            name='image_comp',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='height_field', null=True, upload_to=aktuels.models.upload_location, verbose_name='Aktuel Resmi', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='aktuel',
            name='width_field',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Genişlik Değeri'),
        ),
        migrations.AlterField(
            model_name='aktuelproducts',
            name='height_field',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='aktuelproducts',
            name='image_prod',
            field=versatileimagefield.fields.VersatileImageField(height_field='height_field', null=True, upload_to=aktuels.models.upload_location, width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='aktuelproducts',
            name='width_field',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
