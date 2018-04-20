from django.urls import path
from .views import *

urlpatterns = [

	path('base/',vista_base, name='vista_base'),
	path('mascota/',vista_mascota, name='mascota'),
	path('cliente/',vista_cliente, name='cliente'),
	path('raza/',vista_raza, name='raza'),
	path('servicio/',vista_servicio, name='servicio'),

#=================link de agregar========

	path('agregarMascota/',vista_lista_mascota, name='vista_lista_mascota'),
	path('agregarCliente/',vista_lista_cliente, name='vista_lista_cliente'),
	path('agregarRaza/',vista_lista_raza, name='vista_lista_raza'),
	path('agregarServicio/',vista_lista_servicio, name='vista_lista_servicio'),
	
#=================ver============

	path('verMascota/<int:id_mascota>/',vista_ver_mascota, name='vista_ver_mascota'),
	path('verCliente/<int:id_cliente>/',vista_ver_cliente, name='vista_ver_cliente'),
	path('verRaza/<int:id_raza>/',vista_ver_raza, name='vista_ver_raza'),
	path('verServicio/<int:id_servicio>/',vista_ver_servicio, name='vista_ver_servicio'),

#=============editar===============

	path('editarMascota/<int:id_mascota>/',vista_editar_mascota, name='vista_editar_mascota'),
	path('editarCliente/<int:id_cliente>/',vista_editar_cliente, name='editar_cliente'),
	path('editarRaza/<int:id_raza>/',vista_editar_raza, name='vista_editar_raza'),
	path('editarServicio/<int:id_servicio>/',vista_editar_servicio, name='vista_editar_servicio'),


#=============eliminar===============

	path('eliminarMascota/<int:id_mascota>/',vista_eliminar_mascota, name='vista_eliminar_mascota'),
	path('eliminarCliente/<int:id_cliente>/',vista_eliminar_cliente, name='vista_eliminar_cliente'),
	path('eliminarRaza/<int:id_raza>/',vista_eliminar_raza, name='vista_eliminar_raza'),
	path('eliminarServicio/<int:id_servicio>/',vista_eliminar_servicio, name='vista_eliminar_servicio'),

#==========================login============

	path('', vista_login, name='vista_login'),
	path('logout/' ,vista_logout, name= 'vista_logout'),

#================================registro========

	path('registro/' ,vista_registro, name='vista_registro'),

]