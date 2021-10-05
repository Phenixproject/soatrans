from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *

class Role(models.Model) :
    libelle_role = models.CharField(max_length = 100)

class Utilisateur(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False)
    last_name = models.CharField(max_length=100, blank = False)
    first_name = models.CharField(max_length=100, blank = False)
    CIN = models.CharField(max_length=12, null=True)
    telephone_utilisateur = models.CharField(max_length = 10, blank = False)
    statut_utilisateur = models.BooleanField(default = False, blank = False) # Si l'utilisateur est déjà confirmé
    role = models.ForeignKey(Role, related_name="utilisateur_role", on_delete=models.CASCADE, null="True")

    objects = UtilisateurManager()
    USERNAME_FIELD = 'username'

    #def __str__(self):
        #return "{}{}".format(self.last_name)

class Voiture(models.Model):
    numero_voiture = models.CharField(max_length = 7, blank = False)
    etat_voiture = models.BooleanField(default = True, blank = False)
    utilisateur = models.ForeignKey(Utilisateur, related_name="voiture_utilisateur", on_delete=models.CASCADE)

class Horaire(models.Model):
    heure = models.DateField(null=False)

class Reservation(models.Model):
    montant_paye = models.BigIntegerField(blank = False)
    avance_paye = models.BigIntegerField(blank = False)
    position_place = models.CharField(max_length = 100, blank = False)
    ville_depart = models.CharField(max_length = 100, blank = False)
    ville_destination = models.CharField(max_length = 100, blank = False)
    utilisateur = models.ForeignKey(Utilisateur, related_name="reservation_utilisateur", on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture, related_name="reservation_voiture", on_delete=models.CASCADE)

class Voyage(models.Model) :
    libelle_voyage = models.CharField(max_length = 100, blank = False)
    frais_voyage = models.BigIntegerField(blank = False)
    nombre_place = models.IntegerField(blank = False)
    heure = models.ManyToManyField(Horaire, related_name="voyage_horaire")
