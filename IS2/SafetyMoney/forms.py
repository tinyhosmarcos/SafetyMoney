from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class IniciarSesionForm(AuthenticationForm):
	
	class Meta:
		model = User
	


	
class RegistrarDatosForm(UserCreationForm):
	first_name = forms.CharField(max_length=32)
	last_name = forms.CharField(max_length=32)
	email = forms.EmailField(max_length=64)

	class Meta:
		model = User
		# I've tried both of these 'fields' declaration, result is the same
		# fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
		help_texts = {
			'username': None,
		}
		widgets = {
		'username': forms.TextInput(attrs={'class': 'form-control',}),
		'first_name': forms.TextInput(attrs={'class': 'form-control'}),
		'last_name': forms.TextInput(attrs={'class': 'form-control'}),
		'email': forms.EmailInput(attrs={'class': 'form-control'}),
		'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
		'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
		}

class CambiarDatosForm(UserCreationForm):
	first_name = forms.CharField(max_length=32)
	last_name = forms.CharField(max_length=32)
	email = forms.EmailField(max_length=64)

	class Meta:
		model = User
		# I've tried both of these 'fields' declaration, result is the same
		# fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
		help_texts = {
			'username': None,
		}
		widgets = {
		'username': forms.TextInput(attrs={'class': 'form-control',}),
		'first_name': forms.TextInput(attrs={'class': 'form-control'}),
		'last_name': forms.TextInput(attrs={'class': 'form-control'}),
		'email': forms.EmailInput(attrs={'class': 'form-control'}),
		'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
		'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
		}
