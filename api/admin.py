from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Role)
admin.site.register(Utilisateur)
admin.site.register(Horaire)
admin.site.register(ClasseVoiture)
admin.site.register(Destination)
admin.site.register(HoraireClasse)
admin.site.register(Voiture)
admin.site.register(Reservation)