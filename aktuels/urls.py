from django.urls import path

from .views import (
	AktuelProductsListView
	)


app_name = 'aktuels'

urlpatterns = [
	path('<int:pk>/', AktuelProductsListView.as_view(), name="list"),  # /aktuel/1/
]