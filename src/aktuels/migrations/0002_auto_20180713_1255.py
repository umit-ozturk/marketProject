# Generated by Django 2.0.2 on 2018-07-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aktuels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktuel',
            name='aktuel_company_name',
            field=models.CharField(max_length=140, verbose_name='Aktuel Firma Ismi'),
        ),
        migrations.AlterField(
            model_name='aktuel',
            name='aktuel_company_site',
            field=models.CharField(max_length=140, verbose_name='Aktuel Firma Sitesi'),
        ),
    ]