from django.conf.urls import url
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    url(r'^roles/$', views.all_role),
    url(r'^roles/(?P<pk>[0-9]+)$', views.single_role),
    url(r'^utilisateurs/$', views.all_utilisateur),
    url(r'^utilisateurs/(?P<pk>[0-9]+)$', views.single_utilisateur),
    url(r'^voitures/$', views.all_voiture),
    url(r'^voitures/(?P<pk>[0-9]+)$', views.single_voiture),
    url(r'^reservations/$', views.all_resevation),
    url(r'^reservations/(?P<pk>[0-9]+)$', views.single_reservation),
    url(r'^classevoitures/$', views.all_classevoiture),
    url(r'^classevoitures/(?P<pk>[0-9]+)$', views.single_classevoiture),
    url(r'^horaires/$', views.all_horaire),
    url(r'^horaires/(?P<pk>[0-9]+)$', views.single_horaire),
    url(r'^destinations/$', views.all_destination),
    url(r'^destinations/(?P<pk>[0-9]+)$', views.single_destination),
    url(r'^horaireclasses/$', views.all_horaireclasse),
    url(r'^horaireclasses/(?P<pk>[0-9])$', views.single_horaireclasse),

    #token URL
    url(r'token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^tokenrefresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
