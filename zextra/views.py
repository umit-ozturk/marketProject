from django.db.models import Q
from django.views.generic import (
            DetailView,
            ListView
    )
from .models import Extra_Footer_Contact, Extra_Footer_Head_1, Extra_Footer_Head_2, Extra_Footer_Head_3,\
    Extra_Footer_Bottom_1, Extra_Footer_Bottom_2, Extra_Footer_Bottom_3


class Extra_Footer_ContactListView(ListView):
    extra_footer_contact = Extra_Footer_Contact.objects.all()
    extra_footer_head_1 = Extra_Footer_Head_1.objects.all()
    extra_footer_head_2 = Extra_Footer_Head_2.objects.all()
    extra_footer_head_3 = Extra_Footer_Head_3.objects.all()
    extra_footer_bottom_1 = Extra_Footer_Bottom_1.objects.all()
    extra_footer_bottom_2 = Extra_Footer_Bottom_2.objects.all()
    extra_footer_bottom_3 = Extra_Footer_Bottom_3.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Extra_Footer_Contact.objects.all()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        return
