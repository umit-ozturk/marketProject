from django.urls import path

from .views import(
    TicketDetailView,
    )


app_name = 'products'

urlpatterns = [
    path('<slug:slug>/', TicketDetailView.as_view(), name="ticket"),  # /ticket/slug
]