from django.conf.urls import url
from django.urls import path

from .views import (
	AktuelListView,
	AktuelDetailView
	)



app_name = 'aktuels'

urlpatterns = [
	path('', AktuelListView.as_view(), name="list"), # /aktuel/
	path('<slug:slug>/', AktuelDetailView.as_view(), name="detail"), # /aktuel/slug/
]