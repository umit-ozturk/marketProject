from django.conf.urls import url
from django.urls import path

from .views import  (
    CategoryListView,
    CategoryDetailView
    )


app_name = 'categories'

urlpatterns = [
    path('', CategoryListView.as_view(), name="list"), # /category/
    path('<int:pk>/', CategoryDetailView.as_view(), name="detail"), # /category/1/
]