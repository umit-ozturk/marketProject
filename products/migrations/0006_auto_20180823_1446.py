# Generated by Django 2.0.2 on 2018-08-23 14:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180823_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinfo',
            options={'ordering': ('-created_at',), 'verbose_name': 'Ürün Bilgisi', 'verbose_name_plural': 'Ürün Bilgileri'},
        ),
        migrations.AlterModelManagers(
            name='productinfo',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='productinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Oluşturulma Tarihi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productinfo', to='products.ProductInfo', verbose_name='Ürün Slug / Sayacı'),
        ),
    ]