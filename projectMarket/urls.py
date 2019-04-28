"""projectMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


from accounts.views import UserRegisterView

from products.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name="home"),
    ### APPS
    path('products/', include('products.urls', namespace='product')),
    path('categories/', include('categories.urls', namespace='category')),
    path('companies/', include('companies.urls', namespace='company')),
    path('aktuels/', include('aktuels.urls', namespace='aktuel')),
    path('carts/', include('cart.urls', namespace='cart')),
    path('tickets/', include('tickets.urls', namespace='ticket')),
    #path('companies/', include('companies.urls', namespace='company')),
    ### API

    path('api/category/', include('categories.api.urls', namespace='category-api')),
    path('api/aktuel/', include('aktuels.api.urls', namespace='aktuel-api')),
    path('api/company/', include('companies.api.urls', namespace='company-api')),
    path('register/', UserRegisterView.as_view(), name="register"),
    #path('api/company/', include('companies.api.urls', namespace='company-api')),

    path('', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include('accounts.urls', namespace='profile')),
]


if settings.DEBUG: 
    #urlpatterns += ((static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
