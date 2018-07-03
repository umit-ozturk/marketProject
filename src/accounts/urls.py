from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView

from .views import  (
	ProfileDetailView
    )


app_name = 'profiles'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<str:slug>/', ProfileDetailView.as_view(), name='profile'),
    ]