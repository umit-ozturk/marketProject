# Generated by Django 2.0.2 on 2018-07-24 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='userphoto',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]