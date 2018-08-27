from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField


def upload_location(instance, filename):
    upload_path = "img/ticket/"+ str(filename)
    return upload_path


class Ticket(models.Model):
    ticket_name = models.CharField('Ticket Adı', max_length=280, null=True, blank=True)
    ticket_description = RichTextField('Ticket Açıklaması', max_length=280, null=True, blank=True)
    company = models.ForeignKey("tickets.ticketcompany", verbose_name='Ticketın Firması', on_delete=models.CASCADE,
                                related_name="ticket_company", null=True,  blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Ticketlar'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.ticket_name)


class TicketCompany(models.Model):
    company_name = models.CharField('Ticket Firmasının İsmi', max_length=140, null=True, blank=True)
    company_site = models.CharField('Ticket Firmasının Sitesi', max_length=140, null=True, blank=True)
    company_description = RichTextField('Ticket Firmasının Açıklaması', null=True, blank=True)
    image_comp = models.ImageField('Ticket Firmasının Resmi', upload_to=upload_location, null=True, blank=True,
                                   width_field="width_field", height_field="height_field")
    height_field = models.IntegerField('Uzunluk Değeri', default=0, blank=True)
    width_field = models.IntegerField('Genişlik Değeri', default=0, blank=True)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Ticket Firması'
        verbose_name_plural = 'Ticket Firmaları'
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.company_name)



