from django.conf.urls import url
from . import views

#all_client
#single_reservation(pk)
#all_client_reservations
#all_single_client_reservation(pk)
#single_client_reservation(pk)

urlpatterns = [
    url(r"^$", views.all_client),
    url(r"(?P<pk>[0-9]+)$", views.single_client),
    url(r"^clientsReservations/$", views.all_client_reservations),
    url(r'^allSingleClientReservation/(?P<pk>[0-9]+)$', views.all_single_client_reservation),
    url(r'^tada/(?P<pk>[0-9]+)$', views.tada),
    url(r'^singleClientReservation/(?P<pk>[0-9]+)$', views.single_client_reservation)
]