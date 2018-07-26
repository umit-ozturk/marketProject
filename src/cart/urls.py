from django.conf.urls import url
from django.urls import path

from .views import  (
	get_cart,
	add_to_cart
    )


app_name = 'shopcarts'

urlpatterns = [
    path('cart/', get_cart, name="list"), #/shopcart/
    path('cart/add', add_to_cart, name="add-cart"), #/shopcart/add
    ]
