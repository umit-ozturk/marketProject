from django.conf.urls import url
from django.urls import path

from .views import (
    CompanyListAPIView
    )


app_name = 'categories'

urlpatterns = [
    path('', CompanyListAPIView.as_view(), name="list"),  # /company/
]