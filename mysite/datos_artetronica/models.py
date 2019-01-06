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
	     nombre_de_usuario=models.CharField(max_length=20)
	     pasword=models.CharField(max_length=4)
	     email = models.EmailField(blank=True)
	     nombres=models.CharField(max_length=30)
	     apellidos=models.CharField(max_length=30)
	     plan_contratado=models.CharField(max_length=30,choices=PLANES,default="NINGUNO")
	     estado_del_plan=models.CharField(max_length=30,choices=ESTADO,default="'DE_BAJA")
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)

	     def __str__(self):
		    		return  self.codigo
	     class Admin:
		    		list_display = ('nombre_de_usuario',' plan_contratado','estado_del_plan')


class Colaboradores(models.Model):		
		nombre_de_usuario=models.CharField(max_length=20)
		pasword=models.CharField(max_length=4)
		email = models.EmailField(blank=True)
		nombres=models.CharField(max_length=30)
		apellidos=models.CharField(max_length=30)
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


SEXO = (('M', 'M'),
	   ('F', 'F'),
		       )

RANGO_EDAD = (('JOVEN', 'M'),
	   ('JOVEN_ADULTO', 'F'),
	   ('ADULTO', 'F'),
	   ('ADULTO_MAYOR', 'F'),
	   ('ANCIANO', 'F'),
		       )
GRADO_ACADEMICO = (('NO_ESTUDIO', 'NO_ESTUDIO'),
	   ('EDUCACION_BASICA', 'EDUCACION_BASICA'),
	   ('BACHILLERATO', 'BACHILLERATO'),
	   ('ESTUDIOS_UNIVERSITARIOS', 'ESTUDIOS_UNIVERSITARIOS'),
	   ('PROFESIONAL', 'PROFESIONAL'),
		       )
ESTADO_SOCIOECONOMICO = (('DESEMPLEADO', 'DESEMPLEADO'),
	   ('NEGOCIO_PROPIO', 'NEGOCIO_PROPIO'),
	   ('EMPLEADO_PUBLICO', 'EMPLEADO_PUBLICO'),
	   ('EMPLEADO_PRIVADO', 'EMPLEADO_PRIVADO'),
	   ('TRABAJO_LA_TIERRA', 'TRABAJO_LA_TIERRA'),
	      )

PREFERENCIA = (('FML', 'FML'),
	   ('GAN', 'GAN'),	   
	   ('VAMO', 'VAMO'),
	   ('ALIANZA', 'ALIANZA'),
	   ('AREN', 'AREN'),
	   ('PC', 'PC'),
	   ('PD', 'PD'),
	   ('DSV', 'DSV'),
	  	      )

class Cuestionario_temporal(models.Model):
		Sexo=models.CharField(max_length=2,choices=SEXO)
		Rango_de_edad=models.CharField(max_length=30,choices=RANGO_EDAD)
		Grado_academico=models.CharField(max_length=30,choices=GRADO_ACADEMICO)
		Estado_socioeconomico=models.CharField(max_length=30,choices=ESTADO_SOCIOECONOMICO)
		Departamento_muestra=models.ForeignKey('Departamentos')
		Ciudad_muestra=models.ForeignKey('Ciudades')
		Cual_es_su_preferencia=models.CharField(max_length=60,choices=PREFERENCIA)
		Colaborador=models.CharField(max_length=60,blank=True)
		fecha_ingreso = models.DateField(default=datetime.now,editable = False)
		def __str__(self):
			return  self.Cual_es_su_preferencia
		class Admin:
			list_display = ('Departamento','Sexo','Cual_es_su_preferencia','fecha_ingreso')

class Cuestionario_final(models.Model):
		Sexo=models.CharField(max_length=2,choices=SEXO)
		Rango_de_edad=models.CharField(max_length=30,choices=RANGO_EDAD)
		Grado_academico=models.CharField(max_length=30,choices=GRADO_ACADEMICO)
		Estado_socioeconomico=models.CharField(max_length=30,choices=ESTADO_SOCIOECONOMICO)
		Departamento_muestra=models.ForeignKey('Departamentos')
		Ciudad_muestra=models.ForeignKey('Ciudades')
		Cual_es_su_preferencia=models.CharField(max_length=60,choices=PREFERENCIA)
		Colaborador=models.CharField(max_length=60,blank=True)
		fecha_ingreso = models.DateField(default=datetime.now,editable = False)
		def __str__(self):
			return  self.Cual_es_su_preferencia
		class Admin:
			list_display = ('Departamento','Sexo','Cual_es_su_preferencia','fecha_ingreso')	     


class Datos_a_graficar(models.Model):
	masculino=models.IntegerField(blank=True,default=0)
	femenino=models.IntegerField(blank=True,default=0)
	
	joven=models.IntegerField(blank=True,default=0)
	joven_adulto=models.IntegerField(blank=True,default=0)
	adulto=models.IntegerField(blank=True,default=0)
	adulto_mayor=models.IntegerField(blank=True,default=0)
	anciano=models.IntegerField(blank=True,default=0)
	
	no_estudio=models.IntegerField(blank=True,default=0)
	educacion_basica=models.IntegerField(blank=True,default=0)
	bachillerrato=models.IntegerField(blank=True,default=0)
	estudios_universitarios=models.IntegerField(blank=True,default=0)
	profesional=models.IntegerField(blank=True,default=0)
	
	desempleado =models.IntegerField(blank=True,default=0)
	negocio_propio=models.IntegerField(blank=True,default=0)
	empleado_publico=models.IntegerField(blank=True,default=0)
	empleado_privado=models.IntegerField(blank=True,default=0)
	trabajo_la_tierra=models.IntegerField(blank=True,default=0)
	
	fml=models.IntegerField(blank=True,default=0)
	gan=models.IntegerField(blank=True,default=0)
	vamo=models.IntegerField(blank=True,default=0)
	alianza=models.IntegerField(blank=True,default=0)
	aren=models.IntegerField(blank=True,default=0)
	pc=models.IntegerField(blank=True,default=0)
	pd=models.IntegerField(blank=True,default=0)
	dsv=models.IntegerField(blank=True,default=0)

	def __str__(self):
			return  self.Cual_es_su_preferencia
	class Admin:
			list_display = ('Departamento','Sexo','Cual_es_su_preferencia','fecha_ingreso')	     
