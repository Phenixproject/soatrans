from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['libelle_role']

class UtilisateurSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Utilisateur
        fields = ('username','name','telephone_utilisateur','statut_utilisateur','role')

class VoyageSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Voyage
        fields = ('libelle_voyage','frais_voyage','nombre_place')

class VoitureSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Voiture
        fields = ('numero_voiture', 'etat_voiture', 'utilisateur')

class ReservationSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Reservation
        fields = ('montant_paye', 'avance_paye', 'position_place', 'ville_depart',
                  'ville_destination', 'utilisateur', 'voyage')