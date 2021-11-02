from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *

'''
    VIP
        isakin 2h
        tana-antsirabe
        antsirabe-tana

    Premium
        tana-antsirabe
        tana-ambatolampy
        ambatolampy-tana

        isakin 1h
        mety mande isakin 30min

    Tsotra
        ambatolampy-tamatave
        tamatave-ambatolampy
    {
        "depart" : "Antananarivo",
        "arrive" : "Antsirabe"
    }
    
    {
        "horaire" : 1,
        "classe" : 1
    }

'''

class Role(models.Model) :
    libelle_role = models.CharField(max_length = 100)

class Utilisateur(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False)
    last_name = models.CharField(max_length=100, blank = False)
    first_name = models.CharField(max_length=100, blank = False)
    adresse = models.CharField(max_length=100, blank = False)
    CIN = models.CharField(max_length=12, null=True)
    sexe = models.BooleanField(default=False)
    date_inscription = models.DateTimeField(auto_now_add=True)
    telephone_utilisateur = models.CharField(max_length = 10, blank = False)
    statut_utilisateur = models.BooleanField(default = False, blank = False) # Si l'utilisateur est déjà confirmé

    objects = UtilisateurManager()
    USERNAME_FIELD = 'username'
    
class Local(models.Model):
    local = models.CharField(max_length = 50, blank = False)
    
class Personnel(models.Model):
    username_personnel = models.CharField(max_length = 100, unique = True, blank = False)
    first_name_personne = models.CharField(max_length = 100, blank = False)
    last_name_personnel = models.CharField(max_length = 100, blank = False)
    matricule_personnel = models.CharField(max_length = 4, blank = False)
    CIN_personnel = models.CharField(max_length = 12, blank = False)
    telephone_personnel = models.CharField(max_length = 10, blank = False)
    password_personnel = models.CharField(max_length = 50, blank = False)
    statut_personnel = models.BooleanField(blank = False, default = False)
    local = models.ForeignKey(Local, related_name = "personnel_local", on_delete = models.CASCADE, null = true)
    role = models.ForeignKey(Role, related_name="personnel_role", on_delete=models.CASCADE, null= True)

    #def __str__(self):
        #return "{}{}".format(self.last_name)

class Horaire(models.Model):
    heure = models.CharField(max_length=20, null=False)

class ClasseVoiture(models.Model):
    classe = models.CharField(max_length=20, blank=False, null=False)

class Destination(models.Model):
    depart = models.CharField(max_length=100, blank=False)
    arrive = models.CharField(max_length=100, blank=False)

class HoraireClasse(models.Model):
    horaire = models.ForeignKey(Horaire, related_name="horaireclasse_horaire", on_delete=models.CASCADE)
    classe = models.ForeignKey(ClasseVoiture, related_name="horaireclasse_classevoiture", on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, related_name="horaireclasse_destination", on_delete=models.CASCADE)

class Voiture(models.Model):
    numero_voiture = models.CharField(max_length = 7, blank = False)
    etat_voiture = models.BooleanField(default = True, blank = False)
    classe = models.ForeignKey(ClasseVoiture, related_name="voiture_classevoiture", on_delete=models.CASCADE)


class Reservation(models.Model):
    montant_paye = models.BigIntegerField(blank = False)
    avance_paye = models.BigIntegerField(defaul)
    position_place = models.CharField(max_length = 100, blank = False)
    #modification... Nasiana date ilay izy mba ahafahana mi filtrer an'ny olona nanao reservaiton tamina date iray
    date = models.DateTimeField(auto_now_add = True)
    utilisateur = models.ForeignKey(Utilisateur, related_name="reservation_utilisateur", on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture, related_name="reservation_voiture", on_delete=models.CASCADE)
    horaireclasse = models.ForeignKey(HoraireClasse, related_name="reservation_horaireclasse", on_delete=models.CASCADE)



class Paiement(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    montant = models.IntegerField()
    personnel = models.ForeignKey(Personnel, related_name="montant_personnel", on_delete=models.CASCADE)
    reservaiton = models.ForeignKey(Reservation, related_name="reservations_paiement", on_delete=models.CASCADE)

