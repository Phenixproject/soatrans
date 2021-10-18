from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['libelle_role']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('montant_paye','avance_paye','position_place', 'date','utilisateur','horaireclasse','voiture')


class UtilisateurSerializer(serializers.ModelSerializer):
    reservation_utilisateur = ReservationSerializer(many=True)
    class Meta:
        model = Utilisateur
        fields = ('id','username','first_name','last_name','CIN','telephone_utilisateur','statut_utilisateur','role', 'reservation_utilisateur')
        extra_kwargs = {'password': {'write_only': True}}

class VoitureSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Voiture
        fields = ('numero_voiture', 'etat_voiture', 'classe')

class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaire
        fields = ('id','heure',)

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields =('id','depart','arrive')

class ClasseVoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseVoiture
        fields = ('id', 'classe',)

class HoraireClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoraireClasse
        fields = ('id', 'horaire', 'classe', 'destination',)