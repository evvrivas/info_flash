#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import View
from django import get_version
from django.http import HttpResponse

class Index(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Running Django ' + str(get_version()) + " on OpenShift")


from django.template.loader import get_template
from django.template import Context

from django.template import RequestContext, loader

from django.http import HttpResponse
import datetime

#from books.models import Publisher
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
#from miPagina.books.models import Book
from mysite.settings import MEDIA_URL


from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile 
from django.contrib.auth.decorators import login_required

from mysite.forms import *
from mysite.datos_artetronica.models import *

from django.contrib.auth.models import User  
from django.core.mail import send_mail
#from templates import *
from django.db.models import Q

from django.db import connection
from random import sample
   
   
    
from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import io
from io import *

##########################
import numpy as np
import matplotlib.pyplot as plt
#################################


def datos_departamento(request):

    date=datetime.datetime.now()

    p1=Departamentos(nombre="AHUACHAPAN")   
    p1.save() 

    p2=Ciudades(departamento=p1,nombre="Ahuachapán")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="Apaneca")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="Atiquizaya")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="Concepción de Ataco")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="El Refugio")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="Guaymango")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="Jujutla")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="San Francisco Menéndez")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="San Lorenzo")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="San Pedro Puxtla")
    p2.save()    

    p2=Ciudades(departamento=p1,nombre="Turín")
    p2.save()

    p2=Ciudades(departamento=p1,nombre="Tacuba")
    p2.save()
      
    return render(request,'principal.html',locals())


def logout(request):
    auth.logout(request)    
    return HttpResponseRedirect("/")

def informacion(request):
  return render(request,'informacion.html',locals())

def principal(request):    
    return render(request,'principal.html',locals())

