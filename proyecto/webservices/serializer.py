from rest_framework import serializers
from mascota.models import *

class mascota_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Mascota
		fields=('url','nombre','peso','sexo','edad',)

class cliente_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cliente
		fields=('url','nombre','direccion','telefono','email',)

class raza_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Raza
		fields=('url','nombre',)

class servicio_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Servicio
		fields=('url','nombre','costo',)