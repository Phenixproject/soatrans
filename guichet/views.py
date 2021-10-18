from django.http.response import HttpResponse
from rest_framework import status
from guichet.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


#mila filtrena ireo olona rehetra ao anaty atomobile irey


@api_view(['GET','POST'])
def all_client(request):
    if request.method == "GET":
        clients = Utilisateur.objects.filter(role__libelle_role='clients')
        serials = ClientSerializer(clients, many=True)
        #return JsonResponse(serials.data,safe=False)
        return Response(serials.data)
    elif request.method == "POST":
        serial = ClientSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
        #return JsonResponse(serial.data,safe=False)
        return Response(serial.data)
    else:
        return HttpResponse({"erreur": "page introuvable"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT'])
def single_client(request,pk):
    try:
        client = Utilisateur.objects.get(id=pk)
        if request.method == "GET":
            serial = ClientSerializer(client)
            #return JsonResponse(serial.data, safe=False)
            return Response(serial.data)
        elif request.method == "PUT":
            serial = ClientSerializer(instance=client, data=request.data)
            if serial.is_valid():
                serial.save()
            #return JsonResponse(serial.data, safe=False)
            return Response(serial.data)
    except Utilisateur.DoesNotExist:
        return HttpResponse({'erreur':'page introuvable'},status=status.HTTP_404_NOT_FOUND)


#Liste des clients qui ont reserver
@api_view(['GET','POST'])
def all_client_reservations(request):
    if request.method == "GET":
        reservations = Reservation.objects.filter(utilisateur__role__libelle_role='clients')
        serials = ReservationSerializer(reservations, many=True)
        #return JsonResponse(serials.data,safe=False)
        return Response(serials.data)
    elif request.method == "POST":
        serial = ReservationSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
        #return JsonResponse(serial.data,safe=False)
        return Response(serial.data)
    else:
        return HttpResponse({"erreur": "page introuvable"}, status=status.HTTP_404_NOT_FOUND)


    #Liste des clients qui ont reserver
@api_view(['GET'])
def all_single_client_reservation(request, pk):
    reservations = Reservation.objects.filter(utilisateur__role__libelle_role='clients').filter(utilisateur__id=pk)
    if request.method == "GET":
        serials = ReservationSerializer(reservations, many=True)
        #return JsonResponse(serials.data,safe=False)
        return Response(serials.data)
    else:
        return HttpResponse({"erreur": "page introuvable"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','PUT'])
def single_client_reservation(request, pk):
    try:
        client_reservation = Reservation.objects.get(id=pk)
        if request.method == "GET":
            serial = ReservationSerializer(client_reservation)
            #return JsonResponse(serial.data, safe=False)
            return Response(serial.data)
        elif request.method == "PUT":
            serial = ReservationSerializer(instance=client_reservation, data=request.data)
            if serial.is_valid():
                serial.save()
            #return JsonResponse(serial.data, safe=False)
            return Response(serial.data)
    except Utilisateur.DoesNotExist:
        return HttpResponse({'erreur':'page introuvable'},status=status.HTTP_404_NOT_FOUND)



#Sivana ho an'ireo reservation hoan'ny hora sy fiara iray
@api_view(['GET'])
def all_single_client_reservation(request, pk):
    reservations = Reservation.objects.filter(utilisateur__role__libelle_role='clients').filter(utilisateur__id=pk)
    if request.method == "GET":
        serials = ReservationSerializer(reservations, many=True)
        #return JsonResponse(serials.data,safe=False)
        return Response(serials.data)
    else:
        return HttpResponse({"erreur": "page introuvable"}, status=status.HTTP_404_NOT_FOUND)





