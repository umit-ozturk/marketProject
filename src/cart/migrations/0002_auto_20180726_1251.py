# Generated by Django 2.0.2 on 2018-07-26 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('-creation_date',), 'verbose_name': 'Sepet', 'verbose_name_plural': 'Sepetler'},
        ),
    ]