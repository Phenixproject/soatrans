from django.shortcuts import render
from api.models import *
from .serializers import *
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def all_client(request):
    if request.method == "GET":
        clients = Utilisateur.objects.all()
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

@api_view(['GET','POST'])
def all_classevoiture(request):
    if request.method == "GET":
        classevoitures = ClasseVoiture.objects.all()
        serials = ClasseVoitureSerializer(classevoitures, many=True)
        #return JsonResponse(serials.data,safe=False)
        return Response(serials.data)
    else:
        return HttpResponse({"erreur": "page introuvable"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def list_destination(request, pk):
    if request.method == "GET":
        destinations = HoraireClasse.objects.filter(classe=pk)
        serials = FindDestinationSerializer(destinations, many=True)
        #return JsonResponse(serials.data,safe=False)
        return Response(serials.data)
    else:
        return HttpResponse({"erreur": "page introuvable"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def list_horaire(request,pk):
    if request.method == "GET":
        horaires = Horaire.objects.all()
        serials = HoraireSerializer(horaires, many=True)
        #return JsonResponse(serials.data,safe=False)
        return Response(serials.data)
    else:
        return HttpResponse({"erreur": "page introuvable"}, status=status.HTTP_404_NOT_FOUND)

def authentification(request):
    element = JSONParser().parse(request)
    try:
        client = Utilisateur.objects.get(CIN=element.get('CIN'))
        utilisateur = authenticate(request, username=client.username, password=element.get('password'))
        if utilisateur is not None:
            login(request, utilisateur)
            serial = ClientSerializer(client)
            return JsonResponse(serial.data,safe=False)
        else:
            return HttpResponse('Mot de passe incorrect', status=status.HTTP_400_BAD_REQUEST)
    except Utilisateur.DoesNotExist:
        return HttpResponse('CIN introuvable', status=status.HTTP_400_BAD_REQUEST)