# Generated by Django 2.0.2 on 2018-05-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aktuels', '0002_aktuelproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktuelproducts',
            name='height_field',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='aktuelproducts',
            name='width_field',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
