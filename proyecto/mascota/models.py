from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Cliente(models.Model):
	nombre    = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 100)
	telefono  = models.CharField(max_length = 100)
	email     = models.CharField(max_length = 100)

	def __str__ (self):
		return self.nombre

class Raza(models.Model):
	nombre    = models.CharField(max_length = 100)

	def __str__ (self):
		return self.nombre

class Servicio(models.Model):
	nombre    = models.CharField(max_length  = 100)
	costo     =models.DecimalField(max_digits = 10, decimal_places = 2)

	def __str__ (self):
		return self.nombre

class Mascota(models.Model):
	nombre  = models.CharField(max_length = 100)
	peso    = models.CharField(max_length =  20)
	sexo    = models.CharField(max_length  =  20)
	edad    = models.CharField(max_length  =  20)
	foto    =models.ImageField(upload_to ='medida/foto', null=True, blank= True)

	servicio = models.ManyToManyField(Servicio, null=True, blank=True)
	raza     = models.ForeignKey(Raza, on_delete = models.CASCADE)
	cliente  = models.ForeignKey(Cliente, on_delete = models.CASCADE)
	
	def __str__ (self):
		return self.nombre


#===== modelo user===

class Perfil(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	foto=models.ImageField(upload_to='Perfiles', null=True, blank=True)
	nombre=models.CharField(max_length=100)

	def __str__ (self):
		return self.user.username


