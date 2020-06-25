from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views
app_name='SafetyMoney'
urlpatterns = [
	path('pagina_principal',login_required(views.PaginaPrincipal.as_view()),name='pagina_principal'),
	path('iniciar_sesion',views.IniciarSesion.as_view(),name='iniciar_sesion'),
	path('registrarse',views.ControlRegistro.as_view(),name='vista_registro'),
	path('login/', auth_views.LoginView.as_view(template_name='SafetyMoney/iniciar_sesion.html'),name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='SafetyMoney/iniciar_sesion.html'),name='logout'),
	path('cambiar_datos',views.ControlCuenta.as_view(),name='vista_cuenta'),
	path('ingresos',views.ControlIngresos.as_view(),name='vista_ingresos'),
	path('gastos',views.ControlGastos.as_view(),name='vista_gastos'),
]