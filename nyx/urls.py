from django import urls
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^client/', include('client.urls')),
    url(r'^guichet/', include('guichet.urls')),
]
