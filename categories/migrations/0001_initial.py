# Generated by Django 2.0.2 on 2018-09-06 20:29

import categories.models
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Kategori Ismi')),
                ('category_defination', models.CharField(blank=True, max_length=140, null=True, verbose_name='Kategori Açıklaması')),
                ('category_logo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Kategori Logo')),
                ('category_slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('image_prod', versatileimagefield.fields.VersatileImageField(blank=True, height_field='height_field', null=True, upload_to=categories.models.upload_location, verbose_name='Kategori Resmi', width_field='width_field')),
                ('height_field', models.PositiveIntegerField(blank=True, default=0, verbose_name='Uzunluk Değeri')),
                ('width_field', models.PositiveIntegerField(blank=True, default=0, verbose_name='Genişlik Değeri')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='categories.Category', verbose_name='Üst Kategori')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent', 'category_slug')},
        ),
    ]
