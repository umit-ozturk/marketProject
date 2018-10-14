from django.conf.urls import url
from django.urls import path

from .views import  (
    CompanyListView,
    CompanyDetailView
    )


app_name = 'companies'

urlpatterns = [
    path('', CompanyListView.as_view(), name="list"),  # /company/
    path('<int:pk>/', CompanyDetailView.as_view(), name="detail"),  # /company/1/
]