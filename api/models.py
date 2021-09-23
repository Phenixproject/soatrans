from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *

class Role(models.Model) :
    libelle_role = models.CharField(max_length = 100)

class Utilisateur(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False)
    name = models.CharField(max_length = 100, blank = False)
    telephone_utilisateur = models.CharField(max_length = 10, blank = False)
    statut_utilisateur = models.BooleanField(default = False, blank = False) # Si l'utilisateur est déjà confirmé
    role = models.ForeignKey(Role, related_name="utilisateur_role", on_delete=models.CASCADE, null="True")

    objects = UtilisateurManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return "{}{}".format(self.name)

class Voyage (models.Model) :
    libelle_voyage = models.CharField(max_length = 100, blank = False)
    frais_voyage = models.BigIntegerField(blank = False)
    nombre_place = models.IntegerField(blank = False)


class Voiture (models.Model) :
    numero_voiture = models.CharField(max_length = 7, blank = False)
    etat_voiture = models.BooleanField(default = True, blank = False)
    utilisateur = models.ForeignKey(Utilisateur, related_name="voiture_utilisateur", on_delete=models.CASCADE)


class Reservation (models.Model) :
    montant_paye = models.BigIntegerField(blank = False)
    avance_paye = models.BigIntegerField(blank = False)
    position_place = models.CharField(max_length = 100, blank = False)
    ville_depart = models.CharField(max_length = 100, blank = False)
    ville_destination = models.CharField(max_length = 100, blank = False)
    utilisateur = models.ForeignKey(Utilisateur, related_name="reservation_utilisateur", on_delete=models.CASCADE)
    voyage = models.ForeignKey(Voyage, related_name="voyage_utilisateur", on_delete=models.CASCADE)