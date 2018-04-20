from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *

# Create your views here.

def vista_base(request):
	return render (request,'base.html')

def vista_mascota(request):
	lista = Mascota.objects.filter()
	return render (request,'mascota.html',locals())

def vista_cliente(request):
	lista = Cliente.objects.filter()
	return render (request,'cliente.html',locals())

def vista_raza(request):
	lista = Raza.objects.filter()
	return render (request,'raza.html',locals())

def vista_servicio(request):
	lista = Servicio.objects.filter()
	return render (request,'servicio.html',locals())

#============ Agregar ===========

def vista_lista_mascota(request):
	if request.method == 'POST':
		formulario = agregar_mascota_form(request.POST, request.FILES)
		if formulario.is_valid():
			mas = formulario.save(commit= False)
			mas.status = True
			mas.save()
			formulario.save_m2m()
			return redirect ('/mascota/')
	else:
		formulario = agregar_mascota_form()
	return render (request, 'agregarMascota.html', locals())

def vista_lista_cliente(request):
	if request.method == 'POST':
		formulario = agregar_cliente_form(request.POST, request.FILES)
		if formulario.is_valid():
			mas = formulario.save(commit= False)
			mas.status = True
			mas.save()
			formulario.save_m2m()
			return redirect ('/cliente/')
	else:
		formulario = agregar_cliente_form()
	return render (request, 'agregarCliente.html', locals())

def vista_lista_raza(request):
	if request.method == 'POST':
		formulario = agregar_raza_form(request.POST, request.FILES)
		if formulario.is_valid():
			mas = formulario.save(commit= False)
			mas.status = True
			mas.save()
			formulario.save_m2m()
			return redirect ('/raza/')
	else:
		formulario = agregar_raza_form()
	return render (request, 'agregarRaza.html', locals())

def vista_lista_servicio(request):
	if request.method == 'POST':
		formulario = agregar_servicio_form(request.POST, request.FILES)
		if formulario.is_valid():
			mas = formulario.save(commit= False)
			mas.status = True
			mas.save()
			formulario.save_m2m()
			return redirect ('/servicio/')
	else:
		formulario = agregar_servicio_form()
	return render (request, 'agregarServicio.html', locals())

#=====================VER==============

def vista_ver_mascota(request, id_mascota):
	m = Mascota.objects.get(id=id_mascota)
	return render (request, 'verMascota.html', locals())

def vista_ver_cliente(request, id_cliente):
	c = Cliente.objects.get(id=id_cliente)
	return render (request, 'verCliente.html', locals())

def vista_ver_raza(request, id_raza):
	r = Raza.objects.get(id=id_raza)
	return render (request, 'verRaza.html', locals())

def vista_ver_servicio(request, id_servicio):
	s = Servicio.objects.get(id=id_servicio)
	return render (request, 'verServicio.html', locals())

#=================editar===================

def vista_editar_mascota(request, id_mascota):
	mas=Mascota.objects.get(id=id_mascota)
	if request.method == "POST":
		formulario = agregar_mascota_form(request.POST, request.FILES, instance = mas)
		if formulario.is_valid():
			mas=formulario.save()
			return redirect('/mascota/')
	else:
		formulario = agregar_mascota_form(instance = mas)
	return render (request, 'agregarMascota.html',locals())

def vista_editar_cliente(request, id_cliente):
	mas=Cliente.objects.get(id=id_cliente)
	if request.method == "POST":
		formulario = agregar_cliente_form(request.POST, request.FILES, instance = mas)
		if formulario.is_valid():
			mas=formulario.save()
			return redirect('/cliente/')
	else:
		formulario = agregar_cliente_form(instance = mas)
	return render (request, 'agregarCliente.html',locals())

def vista_editar_raza(request, id_raza):
	mas=Raza.objects.get(id=id_raza)
	if request.method == "POST":
		formulario = agregar_raza_form(request.POST, request.FILES, instance = mas)
		if formulario.is_valid():
			mas=formulario.save()
			return redirect('/raza/')
	else:
		formulario = agregar_raza_form(instance = mas)
	return render (request, 'agregarRaza.html',locals())

def vista_editar_servicio(request, id_servicio):
	mas=Servicio.objects.get(id=id_servicio)
	if request.method == "POST":
		formulario = agregar_Servicio_form(request.POST, request.FILES, instance = mas)
		if formulario.is_valid():
			mas=formulario.save()
			return redirect('/servicio/')
	else:
		formulario = agregar_servicio_form(instance = mas)
	return render (request, 'agregarServicio.html',locals())



#=============eliminar============

def vista_eliminar_mascota(request, id_mascota):
	mas = Mascota.objects.get(id=id_mascota)
	mas.delete()
	return redirect('/mascota/')

def vista_eliminar_cliente(request, id_cliente):
	mas = Cliente.objects.get(id=id_cliente)
	mas.delete()
	return redirect('/cliente/')

def vista_eliminar_raza(request, id_raza):
	mas = Raza.objects.get(id=id_raza)
	mas.delete()
	return redirect('/raza/')

def vista_eliminar_servicio(request, id_servicio):
	mas = Servicio.objects.get(id=id_servicio)
	mas.delete()
	return redirect('/servicio/')

#==========================LOGIN-LOGOUT=============

def vista_login(request):
	usu=""
	cla=""

	if request.method =="POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username= usu, password= cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/base/')
			else:
				msj = "usuario o clave incorrectos"
	formulario = login_form()
	return render (request, 'login.html', locals())


def vista_logout(request):
	logout(request)
	return redirect('/')

#================REGISTRO========

def vista_registro(request):
	formulario = RegisterForm()
	if request.method == 'POST':
		formulario = RegisterForm(request.POST)
		if formulario.is_valid():


			usuario = formulario.cleaned_data['username']
			email = formulario.cleaned_data['email']
			password_one = formulario.cleaned_data['password_one']
			password_two = formulario.cleaned_data['password_two']


			u = User.objects.create_user(username= usuario, email= email, password= password_one)
			u.save()

			msj = "Gracias por registrarse"

			return render(request,'base.html' , locals())

		else:
			return render(request, 'registro.html' ,locals())

	return render(request, 'registro.html' ,locals())