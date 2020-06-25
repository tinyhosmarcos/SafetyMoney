from django.contrib import admin
from django.db import models
from django import forms
from .models import *


admin.site.register(Usuario)
admin.site.register(Ingreso)
admin.site.register(Gasto)
admin.site.register(Categoria)
admin.site.register(Ahorro)
admin.site.register(Grupo)