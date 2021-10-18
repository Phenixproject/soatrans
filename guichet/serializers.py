from api.models import *
from rest_framework import serializers
from client.serializers import *


class ReservationSerializer(serializers.ModelSerializer):
    utilisateur = ClientSerializer(read_only=True)
    class Meta:
        model = Reservation
        fields = ('montant_paye',
                  'avance_paye',
                  'position_place',
                  'date',
                  'utilisateur',
                  'horaireclasse',
                  'voiture')