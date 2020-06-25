from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login as do_login
from django.views.generic.detail import DetailView
from django.contrib.auth import update_session_auth_hash
# Create your views here.
class IniciarSesion(View):

	template_name = 'SafetyMoney/iniciar_sesion.html'
	context={

	}
	def get(self, request, *args, **kwargs):
		form 								=IniciarSesionForm(request.POST)
		self.context['form']				=form
		self.context['iniciar_sesion']		=True
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		form = IniciarSesionForm(data=request.POST)
		if form.is_valid():
			# Recuperamos las credenciales validadas
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			# Verificamos las credenciales del usuario
			user = authenticate(username=username, password=password)

			# Si existe un usuario con ese nombre y contraseña
			if user is not None:
				# Hacemos el login manualmente
				do_login(request, user)
				# Y le redireccionamos a la portada
				return redirect('SafetyMoney:pagina_principal')
		self.context['form']				=form
		self.context['iniciar_sesion']		=False
		return render(request, self.template_name,self.context )

class PaginaPrincipal(View):
	login_required = True
	template_name = 'SafetyMoney/pagina_principal.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		return render(request, self.template_name,self.context )

class ControlRegistro(View):
	template_name = 'SafetyMoney/registro.html'
	context 	  ={

	}
	def get(self,request,*args,**kwargs):
		form 		= RegistrarDatosForm()
		form.fields['password1'].help_text = None
		form.fields['password2'].help_text = None
		self.context['form']				=form
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		form = RegistrarDatosForm(data=request.POST)
		if form.is_valid():
			# Creamos la nueva cuenta de usuario
			user = form.save()
			# Si el usuario se crea correctamente 
			if user is not None:
				# Hacemos el login manualmente
				do_login(request, user)
				# Y le redireccionamos a la portada
				return redirect('SafetyMoney:iniciar_sesion')
		self.context['form']				=form
		return render(request, self.template_name,self.context )	

class ControlCuenta(View):
	login_required=True
	template_name = 'SafetyMoney/cambiar_datos.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		user=User.objects.get(id=request.user.id)
		form= CambiarDatosForm(instance_user=user)
		account=User.objects.get(username=request.user)
		self.context['form']				=form
		self.context['account']				=account
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		user=User.objects.get(id=request.user.id)
		account=User.objects.get(username=user.username)
		form=CambiarDatosForm(request.POST)
		if form.is_valid():
			test=form.save()
			user=User.objects.get(username=test)
			update_session_auth_hash(request, user)
			return redirect('SafetyMoney:vista_cuenta')
		else: #Form is invalid
			print (form.errors) #You have the error list here.
		self.context['form']				=form
		self.context['account']				=account
		return render(request, self.template_name,self.context )

class ControlIngresos(View):
	login_required = True
	template_name = 'SafetyMoney/ingresos.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		user=User.objects.get(id=request.user.id)

		form 						= 	AgregarIngresoForm(instance_user=user.id)
		self.context['form']		=	form
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		user=User.objects.get(id=request.user.id)
		form 						=  AgregarIngresoForm(instance_user=user.id,data=request.POST)
		if form.is_valid():
			print(form)
			print("es valido")
			test=form.save()
			return redirect('SafetyMoney:pagina_principal')
		self.context['form']		=	form
		return render(request, self.template_name,self.context )

class ControlGastos(View):
	login_required = True
	template_name = 'SafetyMoney/gastos.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		user=User.objects.get(id=request.user.id)

		form 						= 	AgregarGastoForm(instance_user=user.id)
		self.context['form']		=	form
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		user=User.objects.get(id=request.user.id)
		form 						=  AgregarGastoForm(instance_user=user.id,data=request.POST)
		if form.is_valid():
			print(form)
			print("es valido")
			test=form.save()
			return redirect('SafetyMoney:pagina_principal')
		self.context['form']		=	form
		return render(request, self.template_name,self.context )
