from mascota.models import *
from .serializer import *
from rest_framework import viewsets

class mascota_viewset(viewsets.ModelViewSet):
	queryset = Mascota.objects.all()
	serializer_class = mascota_serializer

class cliente_viewset(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class= cliente_serializer

class raza_viewset(viewsets.ModelViewSet):
	queryset = Raza.objects.all()
	serializer_class= raza_serializer

class servicio_viewset(viewsets.ModelViewSet):
	queryset = Servicio.objects.all()
	serializer_class= servicio_serializer

