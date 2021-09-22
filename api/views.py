from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view
from django.http import HttpResponse
# Create your views here.


def home(request):
    reponse = "welcome"
    return HttpResponse(request, reponse)
