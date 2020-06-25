from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
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

class CambiarDatosForm(forms.ModelForm):
	username_old=forms.CharField(max_length=32,widget=forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}))
	username=forms.CharField(max_length=32)
	first_name = forms.CharField(max_length=32)
	last_name = forms.CharField(max_length=32)
	email = forms.EmailField(max_length=64)
	password1 = forms.CharField(max_length=32, widget=forms.PasswordInput)
	password2 = forms.CharField(max_length=32,required=False, widget=forms.PasswordInput)

	class Meta:
		model = User
		# I've tried both of these 'fields' declaration, result is the same
		# fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
		fields =['username_old','username','first_name', 'last_name', 'email','password1','password2']
		

	def __init__(self,*args,**kwargs):
		user=kwargs.pop('instance_user',None)
		super(CambiarDatosForm, self).__init__(*args, **kwargs)
		if user:
			self.fields['username_old'].initial	=user.username
			self.fields['username'].initial		=user.username
			self.fields['first_name'].initial	=user.first_name
			self.fields['last_name'].initial	=user.last_name
			self.fields['email'].initial		=user.email

	def clean(self):
		password1		= self.cleaned_data['password1']
		password2		= self.cleaned_data['password2']
		user = authenticate(username=self.cleaned_data['username_old'], password=password1)
		validate_username=User.objects.filter(username=self.cleaned_data['username'])
		if user is None:
			raise ValidationError({'password1': ["Contraseña Actual Invalida",]})
		if validate_username and self.cleaned_data['username']!=self.cleaned_data['username_old']:
			raise ValidationError({'username': ["Nombre de Usuario no disponible",]})
		if password2:
			validate_password(password2)
		return self.cleaned_data   			

	def save(self, commit=True):
		instance = super(CambiarDatosForm, self).save(commit=False)
		if self.cleaned_data['password2']:
			user 	= User.objects.get(username=self.cleaned_data['username_old'])
			print('save')
			user.set_password(self.cleaned_data['password2'])
			user.save()


		if not self.cleaned_data['password2'] or self.cleaned_data['username_old']!=self.cleaned_data['username_old']:
			user 	= User.objects.filter(username=self.cleaned_data['username_old']).update(
			username=self.cleaned_data['username'],
			first_name=self.cleaned_data['first_name'],
			last_name=self.cleaned_data['last_name'],
			email=self.cleaned_data['email'],
			)
	
		return instance

class AgregarIngresoForm(forms.ModelForm):
	categoria=forms.ModelChoiceField(queryset=Categoria.objects.all())
	grupo=forms.ModelChoiceField(queryset=Grupo.objects.all(),required=False)
	ahorro=forms.ModelChoiceField(queryset=Ahorro.objects.all(), required=False)
	class Meta:
		model=Ingreso
		fields=[
			'ahorro',
			'usuario',
			'grupo',
			'categoria',
			'cantidad',
			'descripcion'
		]
		widgets={
			'usuario':forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}),
		}
	def __init__(self,*args,**kwargs):
		usuario 	=kwargs.pop('instance_user',None)
		usuario_2 	=Usuario.objects.get(user=usuario)

		super(AgregarIngresoForm, self).__init__(*args, **kwargs)
		if usuario:
			print(usuario)
			self.fields['categoria']=forms.ModelChoiceField(queryset=Categoria.objects.all())
			self.fields['grupo']=forms.ModelChoiceField(queryset=Grupo.objects.filter(nombre=usuario_2.grupo), required=False)
			self.fields['usuario'].initial = usuario_2.id
			self.fields['ahorro'] = forms.ModelChoiceField(queryset=Ahorro.objects.filter(usuario__user=usuario), required=False)

class AgregarGastoForm(forms.ModelForm):
	categoria=forms.ModelChoiceField(queryset=Categoria.objects.all())
	class Meta:
		model=Gasto
		fields=[
		'usuario',
		'grupo',	
		'categoria',
		'cantidad',
		'descripcion'
		]
		widgets={
			'usuario':forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}),
		}
	def __init__(self,*args,**kwargs):
		usuario 	=kwargs.pop('instance_user',None)
		usuario_2 	=Usuario.objects.get(user=usuario)

		super(AgregarGastoForm, self).__init__(*args, **kwargs)
		if usuario:
			print(usuario)
			self.fields['categoria']=forms.ModelChoiceField(queryset=Categoria.objects.all())
			self.fields['grupo']=forms.ModelChoiceField(queryset=Grupo.objects.filter(nombre=usuario_2.grupo), required=False)
			self.fields['usuario'].initial = usuario_2.id
			