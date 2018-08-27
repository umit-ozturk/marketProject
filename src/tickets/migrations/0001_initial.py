# Generated by Django 2.0.2 on 2018-08-27 21:45

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import tickets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_name', models.CharField(blank=True, max_length=280, null=True, verbose_name='Ticket Adı')),
                ('ticket_description', ckeditor.fields.RichTextField(blank=True, max_length=280, null=True, verbose_name='Ticket Açıklaması')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Ticketlar',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='TicketCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=140, null=True, verbose_name='Ticket Firmasının İsmi')),
                ('company_site', models.CharField(blank=True, max_length=140, null=True, verbose_name='Ticket Firmasının Sitesi')),
                ('company_description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ticket Firmasının Açıklaması')),
                ('image_comp', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=tickets.models.upload_location, verbose_name='Ticket Firmasının Resmi', width_field='width_field')),
                ('height_field', models.IntegerField(blank=True, default=0, verbose_name='Uzunluk Değeri')),
                ('width_field', models.IntegerField(blank=True, default=0, verbose_name='Genişlik Değeri')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Ticket Firması',
                'verbose_name_plural': 'Ticket Firmaları',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='ticket',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_company', to='tickets.TicketCompany', verbose_name='Ticketın Firması'),
        ),
    ]
