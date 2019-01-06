#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=["fecha_ingreso"]

class ColaboradoresForm(ModelForm):#usuario
	class Meta:			
		model=Colaboradores
		exclude=["fecha_ingreso"]
				    
class DepartamentosForm(ModelForm):#tiendas
	class Meta:			
		model=Departamentos
		exclude=["fecha_ingreso"]
		 
class CiudadesForm(ModelForm):#productos
	class Meta:			
		model=Ciudades
		exclude=["fecha_ingreso"]

class Cuestionario_temporalForm(ModelForm):#productos
	class Meta:			
		model=Cuestionario_temporal
		exclude=["fecha_ingreso"]

class Cuestionario_finalForm(ModelForm):#productos
	class Meta:			
		model=Cuestionario_definitivo
		exclude=["fecha_ingreso"]
    
#############################



