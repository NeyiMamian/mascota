from django import forms
from django.contrib.auth.models import User
from .models import *

class agregar_mascota_form(forms.ModelForm):
	class Meta:
		model = Mascota
		fields = '__all__'

class agregar_cliente_form(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'

class agregar_raza_form(forms.ModelForm):
	class Meta:
		model = Raza
		fields = '__all__'

class agregar_servicio_form(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = '__all__'

#=========================formulario-login=========

class login_form(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	clave = forms.CharField(widget=forms.PasswordInput(render_value=True))

#=================formulario de registro de usuario======

class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput())
	email = forms.EmailField(label="Correo Electronico", widget=forms.TextInput()) 
	password_one = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('email ya registrado')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']

		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('password no coinciden')