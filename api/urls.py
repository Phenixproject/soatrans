from django.conf.urls import url
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    url(r'^roles/$', views.all_role),
    url(r'^roles/(?P<pk>[0-9]+)$', views.single_role),
    url(r'^utilisateurs/$', views.all_utilisateur),
    url(r'^utilisateurs/(?P<pk>[0-9]+)$', views.single_utilisateur),
    url(r'^voyages/$', views.all_voyage),
    url(r'^voyages/(?P<pk>[0-9]+)$', views.single_voyage),
    url(r'^voitures/$', views.all_voiture),
    url(r'^voitures/(?P<pk>[0-9]+)$', views.single_voiture),
    url(r'^reservations/$', views.all_resevation),
    url(r'^reservations/(?P<pk>[0-9]+)$', views.single_reservation),

    #token URL
    url(r'token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^tokenrefresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
