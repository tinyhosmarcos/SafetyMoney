from django.urls import path
from . import views
app_name='SafetyMoney'
urlpatterns = [
	path('index',views.IndexView.as_view(),name='index'),
]