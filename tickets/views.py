from .models import TicketCompany
from django.views.generic import (
     ListView,
     DetailView
     )


def global_ticket_detail():
    ticket = TicketCompany.objects.all()
    return ticket


class TicketDetailView(DetailView):
    queryset = TicketCompany.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TicketDetailView, self).get_context_data(*args, **kwargs)
        return context
