# Generated by Django 2.0.2 on 2018-08-26 13:48

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20180823_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ürün Açıklaması')),
                ('feature', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ürün Özellikleri')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Ürün İçeriği',
                'verbose_name_plural': 'Ürün İçerikleri',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='feature',
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productcontact', to='products.ProductContent', verbose_name='Ürün İçeriği'),
        ),
]