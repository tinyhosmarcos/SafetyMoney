from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Grupo(models.Model):
	nombre			=	models.CharField(max_length=20)
	codigo			=	models.CharField(max_length=15)
	def __str__(self):
		return self.nombre
class Usuario(models.Model):
	user 			=	models.OneToOneField(User, on_delete=models.CASCADE)
	grupo 			=	models.ForeignKey(Grupo, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Ahorro(models.Model):
	usuario 		=	models.ForeignKey(Usuario, on_delete=models.CASCADE)
	grupo 			=	models.ForeignKey(Grupo, null=True,blank=True, on_delete=models.CASCADE)
	descripcion		=	models.CharField(max_length=30)
	monto_objetivo	=	models.DecimalField(max_digits=10, decimal_places=4)
	def __str__(self):
		return self.descripcion

class Categoria(models.Model):
	descripcion		=	models.CharField(max_length=30)
	periodo			=	models.IntegerField()
	def __str__(self):
		return self.descripcion

class Ingreso(models.Model):
	ahorro 			=	models.ForeignKey(Ahorro,null=True,blank=True,on_delete=models.CASCADE)
	usuario 		=	models.ForeignKey(Usuario, on_delete=models.CASCADE)
	grupo 			=	models.ForeignKey(Grupo, null=True,blank=True, on_delete=models.CASCADE)
	categoria		=	models.ForeignKey(Categoria,on_delete=models.CASCADE)
	cantidad		=	models.DecimalField(max_digits=10,decimal_places=4)
	descripcion		=	models.CharField(max_length=30)
	fecha			=	models.DateField(auto_now_add=True)
	def __str__(self):
		return self.descripcion

class Gasto(models.Model):
	usuario 		=	models.ForeignKey(Usuario, on_delete=models.CASCADE)
	grupo 			=	models.ForeignKey(Grupo, null=True,blank=True, on_delete=models.CASCADE)
	categoria		=	models.ForeignKey(Categoria,on_delete=models.CASCADE)
	cantidad		=	models.DecimalField(max_digits=10,decimal_places=4)
	descripcion		=	models.CharField(max_length=30)
	fecha			=	models.DateField(auto_now_add=True)
	def __str__(self):
		return self.descripcion

@receiver(post_save, sender=User)
def create_user_usuario(sender, instance, created, **kwargs):
	if created:
		Usuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_usuario(sender, instance, **kwargs):
	instance.usuario.save()