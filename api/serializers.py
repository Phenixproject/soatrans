from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['libelle_role']

class UtilisateurSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Utilisateur
        fields = ('username','first_name','last_name','CIN','telephone_utilisateur','statut_utilisateur','role')
        extra_kwargs = {'password': {'write_only': True}}

class VoitureSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Voiture
        fields = ('numero_voiture', 'etat_voiture', 'utilisateur')

class ReservationSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Reservation
        fields = ('montant_paye', 'avance_paye', 'position_place', 'utilisateur')

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
        fields = ('classe',)

class HoraireClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoraireClasse
        fields = ('horaire', 'classe', 'destination',)