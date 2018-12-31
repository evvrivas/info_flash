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

    depto="AHUACHAPAN"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Ahuachapán","Apaneca","Atiquizaya","Concepción de Ataco","El Refugio","Guaymango","Jujutla","San Francisco Menéndez","San Lorenzo","San Pedro Puxtla","Turín","Tacuba"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()


    depto="SANTA ANA"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Candelaria de la Frontera","Chalchuapa","Coatepeque","El Congo","El Porvenir","Masahuat","Metapán","San Antonio Pajonal","San Sebastián Salitrillo","Santa Ana","Santa Rosa Guachipilín","Santiago de la Frontera","Texistepeque"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()


    depto="SONSONATE"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Acajutla","Armenia","Caluco","Cuisnahuat","Izalco","Juayúa","Nahuizalco","Nahulingo","Salcoatitán","San Antonio del Monte","San Julián","Santa Catarina Masahuat","Santa Isabel Ishuatán","Santo Domingo Guzmán","Sonsonate","Sonzacate"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()


    depto="CHALATENANGO"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Agua Caliente","Arcatao","Azacualpa","Chalatenango","Comalapa","Citalá","Concepción Quezaltepeque","Dulce Nombre de María","El Carrizal","El Paraíso","La Laguna","La Palma","La Reina","Las Vueltas","Nueva Concepción","Nueva Trinidad","Nombre de Jesús","Ojos de Agua","Potonico","San Antonio de la Cruz","San Antonio Los Ranchos","San Fernando","San Francisco Lempa","San Francisco Morazán","San Ignacio","San Isidro Labrador","San José Cancasque","San José Las Flores","San Luis del Carmen","San Miguel de Mercedes","San Rafael","Santa Rita","Tejutla"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()


    depto="CUSCATLAN"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Candelaria","Cojutepeque","El Carmen","El Rosario","Monte San Juan","Oratorio de Concepción","San Bartolomé Perulapía","San Cristóbal","San José Guayabal","San Pedro Perulapán","San Rafael Cedros","San Ramón","Santa Cruz Analquito","Santa Cruz Michapa","Suchitoto","Tenancingo"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()


    depto="SAN SALVADOR"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Aguilares","Apopa","Ayutuxtepeque","Cuscatancingo","Ciudad Delgado","El Paisnal","Guazapa","Ilopango","Mejicanos","Nejapa","Panchimalco","Rosario de Mora","San Marcos","San Martín","San Salvador","Santiago Texacuangos","Santo Tomás","Soyapango","Tonacatepeque"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()
      


    depto="LA LIBERTAD"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Antiguo Cuscatlán","Chiltiupán","Ciudad Arce","Colón","Comasagua","Huizúcar","Jayaque","Jicalapa","La Libertad","Santa Tecla","Nuevo Cuscatlán","San Juan Opico","Quezaltepeque","Sacacoyo","San José Villanueva","San Matías","San Pablo Tacachico","Talnique","Tamanique","Teotepeque","Tepecoyo","Zaragoza"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()


    depto="SAN VICENTE"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Apastepeque","Guadalupe","San Cayetano Istepeque","San Esteban Catarina","San Ildefonso","San Lorenzo","San Sebastián","San Vicente","Santa Clara","Santo Domingo","Tecoluca","Tepetitán","Verapaz"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()

    depto="CABANAS"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Cinquera","Dolores","Guacotecti","Ilobasco","Jutiapa","San Isidro","Sensuntepeque","Tejutepeque","Victoria"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()

    depto="LA PAZ"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Cuyultitán","El Rosario","Jerusalén","Mercedes La Ceiba","Olocuilta","Paraíso de Osorio","San Antonio Masahuat","San Emigdio","San Francisco Chinameca","San Juan Nonualco","San Juan Talpa","San Juan Tepezontes","San Luis Talpa","San Luis La Herradura","San Miguel Tepezontes","San Pedro Masahuat","San Pedro Nonualco","San Rafael Obrajuelo","Santa María Ostuma","Santiago Nonualco","Tapalhuaca","Zacatecoluca"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()

    depto="USULUTAN"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Alegría","Berlín","California","Concepción Batres","El Triunfo","Ereguayquín","Estanzuelas","Jiquilisco","Jucuapa","Jucuarán","Mercedes Umaña","Nueva Granada","Ozatlán","Puerto El Triunfo","San Agustín","San Buenaventura","San Dionisio","San Francisco Javier","Santa Elena","Santa María","Santiago de María","Tecapán","Usulután"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()

    depto="SAN MIGUEL"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Carolina","Chapeltique","Chinameca","Chirilagua","Ciudad Barrios","Comacarán","El Tránsito","Lolotique","Moncagua","Nueva Guadalupe","Nuevo Edén de San Juan","Quelepa","San Antonio del Mosco","San Gerardo","San Jorge","San Luis de la Reina","San Miguel","San Rafael Oriente","Sesori","Uluazapa"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()


    depto="MORAZAN"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Arambala","Cacaopera","Chilanga","Corinto","Delicias de Concepción","El Divisadero","El Rosario","Gualococti","Guatajiagua","Joateca","Jocoaitique","Jocoro","Lolotiquillo","Meanguera","Osicala","Perquín","San Carlos","San Fernando","San Francisco Gotera","San Isidro","San Simón","Sensembra","Sociedad","Torola","Yamabal","Yoloaiquín"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()


    depto="LA UNION"    
    p1=Departamentos(nombre=depto)   
    p1.save() 
    ciudades=["Anamorós","Bolivar","Concepción de Oriente","Conchagua","El Carmen","El Sauce","Intipucá","La Unión","Lislique","Meanguera del Golfo","Nueva Esparta","Pasaquina","Polorós","San Alejo","San José","Santa Rosa de Lima","Yayantique","Yucuaiquín"]
    for i in ciudades:
        p2=Ciudades(departamento=p1,nombre=i)
        p2.save()


    return render(request,'principal.html',locals())


def logout(request):
    auth.logout(request)    
    return HttpResponseRedirect("/")

def informacion(request):
  return render(request,'informacion.html',locals())



def principal(request):    
    return render(request,'principal.html',locals())


def grafico(reques):  
       
        
        VALOR_DEL_GAS= [("A",10),("b",10),("g",10),("f",10),("s",10)]
        nombre_gases=[]
        valor_gases=[]

        for i in VALOR_DEL_GAS:
            nombre_gases.append(i[0])
            valor_gases.append(i[1])

        X= np.arange(len(nombre_gases))
        Y1 = np.asarray(valor_gases)  
        
        plt.figure()

        plt.gca().set_yscale('log')
        plt.bar(X, Y1, facecolor='#9999ff', edgecolor='white')
        SIMBOLO_GAS=["H2","CH4","C2H2","C2H4","C2H6","CO","O2","N2","CO2"]
      
        z=0 
        for x, y in zip(X, Y1):
            plt.text(x, y ,str(y)+ "\n"+SIMBOLO_GAS[z], ha='center', va= 'bottom')
            z=z+1
 
      
        plt.xlabel('Gases combustibles (H2,CH4,C2H2,C2H4,C2H6) +CO +O2 +N2 +CO2 ')
        plt.ylabel('Concentraciones de gas (ppm) ')
        titulo=""
        plt.title(titulo)
        plt.xticks(())

        subplots_adjust(left=0.21)

        plt.savefig(os.path.join(settings.BASE_DIR, 'static/img/imagen.png'))
      

        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  
        
        return HttpResponse (buffer.getvalue(), content_type="Image/png")

 # Store image in a string buffer


