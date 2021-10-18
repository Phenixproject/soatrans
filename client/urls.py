from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.all_client),
    url(r"^(?P<pk>[0-9]+)$", views.single_client),
    url(r"^login/$", views.authentification),
    url(r'^classevoitures/$', views.all_classevoiture),
    url(r'^destinations/(?P<pk>[0-9]+)$', views.list_destination),
    url(r'^horaires/(?P<pk>[0-9]+)$', views.list_horaire),
    url(r'^getreservations/$', views.filter_reservation)
]