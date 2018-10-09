from django.conf.urls import url
from django.urls import path

from .views import (
    cart_add,
    cart_detail,
    cart_remove,
    send_mail_cart,
    cart_opt
    )


app_name = 'carts'

urlpatterns = [
    path('cart/detail/', cart_detail, name="cart_detail"),  # /cart/detail
    path('cart/add/<product_id>/', cart_add, name="cart_add"),  # /cart/add
    path('cart/opt/<product_id>/', cart_opt, name="cart_opt"),  # /cart/opt
    path('cart/delete/<product_id>/', cart_remove, name="cart_remove"),  # /cart/delete
    path('cart/send/', send_mail_cart, name="cart_send"),  # /cart/send
]
