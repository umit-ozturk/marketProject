from django.conf.urls import url
from django.urls import path

from .views import  (
	cart_add,
	cart_detail,
	cart_remove
    )


app_name = 'carts'

urlpatterns = [
	path('cart/detail/<account_name>/', cart_detail, name="cart_detail"), #/shopcart/detail
    path('cart/add/<product_id>/', cart_add, name="cart_add"), #/shopcart/add
    path('cart/delete/<product_id>/', cart_remove, name="cart_remove"), #/shopcart/delete
    ]
