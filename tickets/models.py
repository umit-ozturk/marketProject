from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField


def upload_location(filename, instance):
    upload_path = "img/ticket/" + str(filename) + str(instance)
    return upload_path


class TicketCompany(models.Model):
    slug = models.SlugField('Ticket Slug', blank=True, unique=True)
    ticket = models.ForeignKey("tickets.ticket", verbose_name='Ticket', on_delete=models.CASCADE,
                                related_name="tickets", null=True,  blank=True)
    company_name = models.CharField('Ticket Firmasının İsmi', max_length=140, null=True, blank=True)
    company_site = models.CharField('Ticket Firmasının Sitesi', max_length=140, null=True, blank=True)
    company_description = RichTextField('Ticket Firmasının Açıklaması', null=True, blank=True)
    image_ticket_comp = VersatileImageField('Ticket Firmasının Resmi', upload_to=upload_location, null=True, blank=True,
                                            width_field="width_field", height_field="height_field")
    height_field = models.PositiveIntegerField('Uzunluk Değeri', default=0, blank=True)
    width_field = models.PositiveIntegerField('Genişlik Değeri', default=0, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Ticket Firması'
        verbose_name_plural = 'Ticket Firmaları'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.company_name)


class Ticket(models.Model):
    ticket_name = models.CharField('Ticket Adı', max_length=280, null=True, blank=True)
    ticket_description = RichTextField('Ticket Açıklaması', max_length=280, null=True, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Ticketlar'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.ticket_name)



