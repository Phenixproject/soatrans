from django.db import models

# Create your models here.

class Role (models.Model) :
    libelle_role = models.CharField(max_length = 100)

class Utilisateur (models.Model) :
    nom_utilisateur = models.CharField(max_length = 100, blank = False)
    telephone_utilisateur = models.CharField(max_length = 10, blank = False)
    mdp_utilisateur = models.CharField(max_length = 50, blank = False)
    statut_utilisateur = models.BooleanField(default = False, blank = False) # Si l'utilisateur est déjà confirmé

class Reservation (models.Model) :
    numero_voiture = models.CharField(max_length = 7, blank = False)
    etat_voiture = models.BooleanField(default = True, blank = False)

class Reservation (models.Model) :
    montant_paye = models.BigIntegerField(blank = False)
    avance_paye = models.BigIntegerField(blank = False)
    position_place = models.CharField(blank = False)
    ville_depart = models.CharField(blank = False)
    ville_destination = models.CharField(blank = False)

class Voyage (models.Model) :
    libelle_voyage = models.CharField(blank = False)
    frais_voyage = models.BigIntegerField(blank = False)
    nombre_place = models.IntegerField(blank = False)