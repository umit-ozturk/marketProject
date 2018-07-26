from django.conf.urls import url
from django.urls import path

from .views import  (
	cart_add,
	cart_detail,
	cart_remove
    )


app_name = 'shopcarts'

urlpatterns = [
	path('cart/detail/', cart_detail, name="detail"), #/shopcart/detail
    path('cart/add/<int:pk>/', cart_add, name="add-cart"), #/shopcart/add
    path('cart/delete/<int:pk>/', cart_remove, name="delete-cart"), #/shopcart/delete
    ]
