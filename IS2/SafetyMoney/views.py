from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.detail import DetailView
# Create your views here.
class IndexView(View):

	template_name = 'SafetyMoney/index.html'
	context={

	}
	def get(self, request, *args, **kwargs):
		
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		return render(request, self.template_name,self.context)

