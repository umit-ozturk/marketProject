from django.conf.urls import url
from django.urls import path

from .views import  (
	UserDetailView,
	UserUpdateView
    )


app_name = 'profiles'

urlpatterns = [
    path('profile/<str:slug>/', UserDetailView.as_view(), name='profile'),
    path('profile/<str:slug>/update/', UserUpdateView.as_view(), name='profile-update'),
    ]