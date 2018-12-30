
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from mysite.datos_artetronica.models import *

#admin.site.unregister(User)
from mysite.forms import *

admin.site.register(Usuarios)
class RulesAdmin(admin.ModelAdmin):
    form = UsuariosForm

###################  cel #####################
admin.site.register(Colaboradores)
class RulesAdmin(admin.ModelAdmin):
    form = ColaboradoresForm

admin.site.register(Departamentos)
class RulesAdmin(admin.ModelAdmin):
    form = DepartamentosForm

admin.site.register(Ciudades)
class RulesAdmin(admin.ModelAdmin):
    form = CiudadesForm

admin.site.register(Cuestionario_temporal)
class RulesAdmin(admin.ModelAdmin):
    form = Cuestionario_temporalForm

admin.site.register(Cuestionario_definitivo)
class RulesAdmin(admin.ModelAdmin):
    form = Cuestionario_definitivoForm
 
 ##########################
   
