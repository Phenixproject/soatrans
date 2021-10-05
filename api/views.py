from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializers import *

''' 
    izao avy ny modification nataoko tato :
        - le single_zvtr nisy diso kely le izy fa
        ts serializer no parametre an le JSONResponse
        f objet python de nosoloiko serializer
        -Commentéko daol aloha le JSONResponse an
        n view rehetra f ho avadiko Response an
        le restframework daol le return an n view
        rehetra de mba mahazo api itestena anazy
        -Namorona view mifanaraka @ le horaire
        
        remarque : rehefa tsy mapiasa ilay API 
                    rest_framework miteste view 
                    f insomnia de tsy maints 
                    manao securité ana format 
                    requete aloha, forcéna ho 
                    parséna JSON le requete,
                    otran le niteste an le view 
                    @ zay mba tena JSON no 
                    miditra ao @ serializer
                    
                    Exemple: 
                        element = JSONParser().parse(requete)
                        serial = RoleSerializer(data=element)
                        
    signé Brice
    PS: Bisous daol :* mazoto miasa XD
'''

@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated, ))
def all_utilisateur(request):
    if request.method == "GET":
        utilisateurs = Utilisateur.objects.all()
        serials = UtilisateurSerializer(utilisateurs, many=True)
        #return JsonResponse(serials.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serials.data)
    elif request.method == "POST":
        serial = UtilisateurSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
        #return JsonResponse(serial.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serial.data)

@api_view(['GET', 'PUT'])
#@permission_classes((IsAuthenticated, ))
def single_utilisateur(request,pk):
    try:
        utilisateur = Utilisateur.objects.get(id=pk)
        #eto le misy diso n an aro f adinony namadika an le
        #zvtr eto ambony ito ho serializer alohan'ny manao
        #return
        if request.method == "GET":
            #return JsonResponse(utilisateur.data, safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front
            return Response(UtilisateurSerializer(utilisateur).data)
        elif request.method == "PUT":
            serial = UtilisateurSerializer(instance=utilisateur, data=request.data)
            if serial.is_valid():
                serial.save()
            #return JsonResponse(serial.data, safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(serial.data)
        else:
            utilisateur.delete()
            return HttpResponse({'message':"l'utilisateur n'existe pas"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated, ))
def all_role(request):
    if request.method == "GET":
        roles = Role.objects.all()
        serials = RoleSerializer(roles, many=True)
        #return JsonResponse(serials.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serials.data)
    elif request.method == "POST":
        serial = RoleSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
        #return JsonResponse(serial.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serial.data)

@api_view(['GET', 'PUT'])
#@permission_classes((IsAuthenticated, ))
def single_role(request, pk):
    try:
        role = Role.objects.get(id=pk)
        # eto le misy diso n an aro f adinony namadika an le
        # zvtr eto ambony ito ho serializer alohan'ny manao
        # return @ le methode get
        if request.method == "GET":
            #return JsonResponse(role.data, safe=False)
            return Response(RoleSerializer(role))
        elif request.method == "PUT":
            serial = RoleSerializer(instance=role, data=request.data)
            if serial.is_valid():
                serial.save()
            #return JsonResponse(serial.data, safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(serial.data)
        else:
            role.delete()
            return HttpResponse({'message':"ce role n'existe pas"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated, ))
def all_voyage(request):
    if request.method == "GET":
        voyages = Voyage.objects.all()
        serials = VoyageSerializer(voyages, many=True)
        #return JsonResponse(serials.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serials.data)
    elif request.method == "POST":
        serial = VoyageSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
        #return JsonResponse(serial.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serial.data)

@api_view(['GET', 'PUT'])
#@permission_classes((IsAuthenticated, ))
def single_voyage(request, pk):
    try:
        role = Voyage.objects.get(id=pk)
        # eto le misy diso n an aro f adinony namadika an le
        # zvtr eto ambony ito ho serializer alohan'ny manao
        # return @ le methode get
        if request.method == "GET":
            #return JsonResponse(role.data, safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(RoleSerializer(role))
        elif request.method == "PUT":
            serial = VoyageSerializer(instance=role,data=request.data)
            if serial.is_valid():
                serial.save()
            #return JsonResponse(serial.data, safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(serial.data)
        else:
            role.delete()
            return HttpResponse({'message':"ce voyage n'existe pas"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated, ))
def all_voiture(request):
    if request.method == "GET":
        voitures = Voiture.objects.all()
        serials = VoitureSerializer(voitures, many=True)
        #return JsonResponse(serials.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serials.data)
    elif request.method == "POST":
        serial = VoitureSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
        #return JsonResponse(serial.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serial.data)

@api_view(['GET', 'PUT'])
#@permission_classes((IsAuthenticated, ))
def single_voiture(request, pk):
    try:
        role = Voiture.objects.get(id=pk)
        # eto le misy diso n an aro f adinony namadika an le
        # zvtr eto ambony ito ho serializer alohan'ny manao
        # return @ le methode get
        if request.method == "GET":
            #return JsonResponse(role.data, safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(role.data)
        elif request.method == "PUT":
            serial = VoitureSerializer(instance=role, data=request.data)
            if serial.is_valid():
                serial.save()
            #return JsonResponse(serial.data, safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(serial.data)
        else:
            role.delete()
            return HttpResponse({'message':"la voiture que vous cherchez n'existe pas"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated, ))
def all_resevation(request):
    if request.method == "GET":
        reservations = Reservation.objects.all()
        serials = ReservationSerializer(reservations, many=True)
        #return JsonResponse(serials.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serials.data)
    elif request.method == "POST":
        serial = ReservationSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
        #return JsonResponse(serial.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serial.data)

@api_view(['GET', 'PUT'])
#@permission_classes((IsAuthenticated, ))
def single_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(id=pk)
        # eto le misy diso n an aro f adinony namadika an le
        # zvtr eto ambony ito ho serializer alohan'ny manao
        # return @ le methode get
        if request.method == "GET":
            #return JsonResponse(role.data, safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(Reservation(reservation).data)
        elif request.method == "PUT":
            serial = ReservationSerializer(instance=reservation, data=request.data)
            if serial.is_valid():
                serial.save()
            #return JsonResponse(serial.data, safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(serial.data)
        else:
            reservation.delete()
            return HttpResponse({'message':"reservation inexistant"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated, ))
def all_horaire(request):
    if request.method == "GET":
        horaires = Horaire.objects.all()
        serials = HoraireSerializer(horaires, many=True)
        #return JsonResponse(serials.data, safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serials.data)
    elif request.method == "POST":
        serial = HoraireSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
        #return JsonResponse(serial.data,safe=False)
        # avadika JsonResponse @ izay le izy rehefa vita teste
        # ka ampifandraisina @ le front de fafana
        # le Response eo ambany
        return Response(serial.data)

@api_view(['GET','PUT'])
def single_horaire(request, pk):
    try:
        horaire = Horaire.objects.get(id=pk)
        # eto le misy diso n an aro f adinony namadika an le
        # zvtr eto ambony ito ho serializer alohan'ny manao
        # return @ le methode get
        if request.method == "GET":
            #return JsonResponse(HoraireSerializer(horaire).data)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(HoraireSerializer(horaire).data)
        elif request.method == "PUT":
            serial = HoraireSerializer(instance=horaire,data=request.data)
            if serial.is_valid():
                serial.save()
            #return JsonResponse(serial.data,safe=False)
            # avadika JsonResponse @ izay le izy rehefa vita teste
            # ka ampifandraisina @ le front de fafana
            # le Response eo ambany
            return Response(serial.data)
        else:
            horaire.delete()
            return HttpResponse({'message': "reservation inexistant"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)






