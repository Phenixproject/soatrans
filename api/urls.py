from django.conf.urls import include,url
from django.urls.conf import path
from . import views


urlpatterns = [
    url('^users/$',views.home)
]
