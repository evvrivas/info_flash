#!/usr/bin/python -tt
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from datetime import datetime 

from django.contrib.auth.models import User
#import Image

from PIL import Image as Img

from io import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from sorl.thumbnail import ImageField



PLANES=(   	('BASICO', 'BASICO'),
			('INTERMEDIO', 'INTERMEDIO'),
			('PRIVILEGIADA', 'PRIVILEGIADA'),
			('NINGUNO', 'NINGUN0'),
		     )
ESTADO=(   	('DE_BAJA', 'DE_BAJA'),
			('DE_ALTA', 'DE_ALTA'),			
		     )

class Usuarios(models.Model):
	     nombre_de_usuario=models.IntegerField()
	     pasword=models.CharField(max_length=4)
	     email = models.EmailField(blank=True)
	     plan_contratado=models.CharField(max_length=30,choices=PLANES,default="NINGUNO")
	     estado_del_plan=models.CharField(max_length=30,choices=ESTADO,default="'DE_BAJA")
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)

	     def __str__(self):
		    		return  self.codigo
	     class Admin:
		    		list_display = ('nombre_de_usuario',' plan_contratado','estado_del_plan')


class Colaboradores(models.Model):
		imagen1 = ImageField(upload_to='tmp',blank=True)
		nombre_de_usuario=models.IntegerField()
		pasword=models.CharField(max_length=4)
		email = models.EmailField(blank=True)
		telefono_whatsapp=models.CharField(max_length=30)
		estado_colaborador=models.CharField(max_length=30,choices=ESTADO,default="'DE_BAJA")
		fecha_ingreso = models.DateField(default=datetime.now,editable = False)
		def __str__(self):
		   		return  self.nombre_de_usuario
		class Admin:
			list_display = ('nombre_de_usuario','telefono_whatsapp','estado_colaborador')

class Departamentos(models.Model):	     
	     nombre=models.CharField(max_length=60,blank=True)	     
	     def __str__(self):
		    		return  self.nombre
	     class Admin:
		    		list_display = ('nombre')

class Ciudades(models.Model):	     
	     departamento=models.ForeignKey('Departamentos',blank=True,null=True)
	     nombre=models.CharField(max_length=60,blank=True)


	     def __str__(self):
		    		return  self.nombre
	     class Admin:
		    		list_display = ('nombre')
categoria=models.ForeignKey('Categoria',blank=True,null=True)

class Cuestionario_temporal(models.Model):
		Sexo=models.CharField(max_length=2,blank=True)
		Rango_de_edad=models.CharField(max_length=30,blank=True)
		Grado_academico=models.CharField(max_length=30,blank=True)
		Estado_socioeconomico=models.CharField(max_length=30,blank=True)
		Departamento_muestra=models.ForeignKey('Departamentos',blank=True,null=True)
		Ciudad_muestra=models.ForeignKey('Ciudades',blank=True,null=True)
		Cual_es_su_preferencia=models.CharField(max_length=60,blank=True)
		Colaborador=models.CharField(max_length=60,blank=True)
		fecha_ingreso = models.DateField(default=datetime.now,editable = False)
		def __str__(self):
			return  self.Cual_es_su_preferencia
		class Admin:
			list_display = ('Departamento','Sexo','Cual_es_su_preferencia','fecha_ingreso')
class Cuestionario_definitivo(models.Model):
		Sexo=models.CharField(max_length=2,blank=True)
		Rango_de_edad=models.CharField(max_length=30,blank=True)
		Grado_academico=models.CharField(max_length=30,blank=True)
		Estado_socioeconomico=models.CharField(max_length=30,blank=True)
		Departamento_muestra=models.ForeignKey('Departamentos',blank=True,null=True)
		Ciudad_muestra=models.ForeignKey('Ciudades',blank=True,null=True)
		Cual_es_su_preferencia=models.CharField(max_length=60,blank=True)
		Colaborador=models.CharField(max_length=60,blank=True)
		fecha_ingreso = models.DateField(default=datetime.now,editable = False)
		def __str__(self):
			return  self.Cual_es_su_preferencia
		class Admin:
			list_display = ('Departamento','Sexo','Cual_es_su_preferencia','fecha_ingreso')	     




