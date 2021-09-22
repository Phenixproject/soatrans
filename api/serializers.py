from rest_framework import serializers
from .models import *

class RoleSerializer(serializers) :
    class Meta:
        models = Role
        fields = ('libelle_role')

class UtilisateurSerializer (models.Model) :
    class Meta:
        models = Utilisateur
        fields = ('nom_utilisateur','telephone_utilisateur','mdp_utilisateur','statut_utilisateur','role')

class VoyageSerializer(models.Model) :
    class Meta:
        models = Voyage
        fields = ('libelle_voyage','frais_voyage','nombre_place')

class VoitureSerializer(models.Model) :
    class Meta:
        models = Voiture
        fields = ('numero_voiture', 'etat_voiture', 'utilisateur')

class ReservationSerializer(models.Model) :
    class Meta:
        models = Reservation
        fields = ('montant_pay', 'avance_paye', 'position_place', 'ville_depart',
                  'ville_destination', 'utilisateur', 'voyage')