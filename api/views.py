from django.http.response import JsonResponse
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import *

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def all_utilisateur(request):
    if request.method == "GET":
        utilisateurs = Utilisateur.objects.all()
        serials = UtilisateurSerializer(utilisateurs, many=True)
        return JsonResponse(serials.data, safe=False)
    elif request.method == "POST":
        serial = UtilisateurSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
        return JsonResponse(serial.data, safe=False)

@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated, ))
def single_utilisateur(request, pk):
    try:
        utilisateur = Utilisateur.objects.get(id=pk)
        if request.method == "GET":
            return JsonResponse(utilisateur.data, safe=False)
        elif request.method == "PUT":
            serial = UtilisateurSerializer(instance=utilisateur, data=request.data)
            if serial.is_valid():
                serial.save()
            return JsonResponse(serial.data, safe=False)
        else:
            utilisateur.delete()
            return HttpResponse({'message':"l'utilisateur n'existe pas"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def all_role(request):
    if request.method == "GET":
        roles = Role.objects.all()
        serials = UtilisateurSerializer(roles, many=True)
        return JsonResponse(serials.data, safe=False)
    elif request.method == "POST":
        serial = RoleSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
        return JsonResponse(serial.data, safe=False)

@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated, ))
def single_role(request, pk):
    try:
        role = Role.objects.get(id=pk)
        if request.method == "GET":
            return JsonResponse(role.data, safe=False)
        elif request.method == "PUT":
            serial = UtilisateurSerializer(instance=role, data=request.data)
            if serial.is_valid():
                serial.save()
            return JsonResponse(serial.data, safe=False)
        else:
            role.delete()
            return HttpResponse({'message':"ce role n'existe pas"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def all_voyage(request):
    if request.method == "GET":
        voyages = Voyage.objects.all()
        serials = UtilisateurSerializer(voyages, many=True)
        return JsonResponse(serials.data, safe=False)
    elif request.method == "POST":
        serial = VoyageSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
        return JsonResponse(serial.data, safe=False)

@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated, ))
def single_voyage(request, pk):
    try:
        role = Voyage.objects.get(id=pk)
        if request.method == "GET":
            return JsonResponse(role.data, safe=False)
        elif request.method == "PUT":
            serial = VoyageSerializer(instance=role, data=request.data)
            if serial.is_valid():
                serial.save()
            return JsonResponse(serial.data, safe=False)
        else:
            role.delete()
            return HttpResponse({'message':"ce voyage n'existe pas"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def all_voiture(request):
    if request.method == "GET":
        voitures = Voiture.objects.all()
        serials = UtilisateurSerializer(voitures, many=True)
        return JsonResponse(serials.data, safe=False)
    elif request.method == "POST":
        serial = VoitureSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
        return JsonResponse(serial.data, safe=False)

@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated, ))
def single_voiture(request, pk):
    try:
        role = Voiture.objects.get(id=pk)
        if request.method == "GET":
            return JsonResponse(role.data, safe=False)
        elif request.method == "PUT":
            serial = VoitureSerializer(instance=role, data=request.data)
            if serial.is_valid():
                serial.save()
            return JsonResponse(serial.data, safe=False)
        else:
            role.delete()
            return HttpResponse({'message':"la voiture que vous cherchez n'existe pas"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def all_resevation(request):
    if request.method == "GET":
        reservation = Reservation.objects.all()
        serials = UtilisateurSerializer(reservation, many=True)
        return JsonResponse(serials.data, safe=False)
    elif request.method == "POST":
        serial = ReservationSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
        return JsonResponse(serial.data, safe=False)

@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated, ))
def single_reservation(request, pk):
    try:
        role = Reservation.objects.get(id=pk)
        if request.method == "GET":
            return JsonResponse(role.data, safe=False)
        elif request.method == "PUT":
            serial = ReservationSerializer(instance=role, data=request.data)
            if serial.is_valid():
                serial.save()
            return JsonResponse(serial.data, safe=False)
        else:
            role.delete()
            return HttpResponse({'message':"reservation inexistant"}, status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)





