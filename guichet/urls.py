from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^clients/$", views.all_client),
    url(r"^clients/(?P<pk>[0-9]+)$", views.single_client),
    url(r"^clientsReservations/$", views.all_client_reservations),
    url(r'^allSingleClientReservation/(?P<pk>[0-9]+)$', views.all_single_client_reservation),
    url(r'^singleClientReservation/(?P<pk>[0-9]+)$', views.single_client_reservation)
]