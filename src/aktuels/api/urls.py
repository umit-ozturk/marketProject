from django.conf.urls import url
from django.urls import path

from .views import  (
	AktuelListAPIView,
	AktuelDetailAPIView
    )


app_name = 'aktuels-api'

urlpatterns = [
    path('', AktuelListAPIView.as_view(), name="list"), # /api/aktuel/
    path('<int:pk>/', AktuelDetailAPIView.as_view(), name="detail"), # /api/aktuel/id/

]