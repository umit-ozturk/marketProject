# Generated by Django 2.0.2 on 2018-07-13 13:16

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_defination',
            field=models.CharField(blank=True, max_length=140, verbose_name='Kategori Açıklaması'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=30, verbose_name='Kategori Ismi'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='categories.Category', verbose_name='Üst Kategori'),
        ),
    ]