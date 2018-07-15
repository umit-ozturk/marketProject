from django.conf.urls import url
from django.urls import path

from .views import  (
	UserDetailView,
    )


app_name = 'profiles'

urlpatterns = [
    path('profile/<str:slug>/', UserDetailView.as_view(), name='profile'),
    ]