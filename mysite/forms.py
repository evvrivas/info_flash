#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=["fecha_ingreso","estado_del_plan"]

class ColaboradoresForm(ModelForm):#usuario
	class Meta:			
		model=Colaboradores
		exclude=["fecha_ingreso","estado_colaborador"]
				    
class DepartamentosForm(ModelForm):#tiendas
	class Meta:			
		model=Departamentos
		exclude=["fecha_ingreso"]


		 
class CiudadesForm(ModelForm):#productos
	class Meta:			
		model=Ciudades
		exclude=["fecha_ingreso"]

	def __init__(self,*args, **kwargs):
		super(CiudadesForm, self).__init__(*args, **kwargs)
		self.fields['departamento'].queryset=Departamentos.objects.all()
		#self.fields['ccomercial'].queryset=Ccomercial.objects.filter(id_usuario=user)


class Cuestionario_temporalForm(ModelForm):#productos
	class Meta:			
		model=Cuestionario_temporal
		exclude=["fecha_ingreso","Colaborador"]

class Cuestionario_finalForm(ModelForm):#productos
	class Meta:			
		model=Cuestionario_final
		exclude=["fecha_ingreso","Colaborador"]

class Datos_a_graficarForm(ModelForm):#productos
	class Meta:			
		model=Datos_a_graficar
		exclude=[""]
		
class Configuracion_sistemaForm(ModelForm):
	class Meta:
			
		model=Configuracion_sistema
		widgets = {'mensaje_bienvenida': Textarea(attrs={'cols': 30, 'rows': 3}),'respuesta': Textarea(attrs={'cols': 30, 'rows': 3}),}
		exclude=[]
#############################



