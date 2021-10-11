from api.serializers import  *
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id','username','first_name','last_name','CIN','telephone_utilisateur','statut_utilisateur','role')
        extra_kwargs = {'password': {'write_only': True}}

class FindHoraireSerializer(serializers.ModelSerializer):
    horaire = HoraireSerializer(many=True)
    class Meta:
        model = HoraireClasse
        fields = ('horaire',)

class FindDestinationSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer()
    class Meta:
        model = HoraireClasse
        fields = ('destination',)

class ClasseVoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseVoiture
        fields = ('id','classe')

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = ('numero_voiture','etat_voiture','classe')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('montant_paye','avance_paye','position_place', 'date','utilisateur','horaireclasse','voiture')

'''
{
        "username": "zexhior",
        "first_name": "Rasolonjatovo",
        "last_name": " Brice Herizo",
        "CIN": "00001111222",
        "telephone_utilisateur": "0347848654",
        "statut_utilisateur": false,
        "role": 1,
        "password": "souvenir123perdu"
    }
'''