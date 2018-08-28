from django.shortcuts import render
from .models import Ticket


# Create your views here.



def global_ticket_detail():
    ticket = Ticket.objects.all()
    return ticket