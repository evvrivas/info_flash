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
import os
from django.conf import settings

from io import BytesIO
import base64
import matplotlib
matplotlib.use("Agg")


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



def us(request):
    date=datetime.datetime.now()
    p1=Usuarios(nombre_de_usuario="MARIO",  pasword="1234",  email ="evvrivas@gmail.com", nombres="mario marlon",  apellidos="reyes", plan_contratado="PRIVILEGIADA", estado_del_plan="DE_ALTA", fecha_ingreso =date )
    p1.save()
    user = User.objects.create_user(username="MARIO", password="1234",email="evvrivas@gmail.com",first_name="mario marlon",last_name="reyes")
    user.save() 


    p1=Colaboradores(nombre_de_usuario="MARIOc", pasword="1234", email ="evvrivas@gmail.com" ,nombres="mario marlonc",apellidos="reyesc",telefono_whatsapp="78218224", estado_colaborador="DE_ALTA", fecha_ingreso =date)
    p1.save()
    user = User.objects.create_user(username="MARIOc", password="1234",email="evvrivas@gmail.com",first_name="mario marlonc",last_name="reyesc")
    user.save() 
    return render(request,'principal.html',locals())

def cues(request):  


    sity=Ciudades.objects.get(id=1)
    sity2=Ciudades.objects.get(id=4)
    date=datetime.datetime.now()    

    p1=Cuestionario_temporal(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia="VAMO",Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_temporal(Sexo="F",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity2,Cual_es_su_preferencia="GAN",Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_temporal(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia="AREN",Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_temporal(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity2,Cual_es_su_preferencia="FML",Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_temporal(Sexo="F",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia="FML",Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_temporal(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia="GAN",Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_temporal(Sexo="F",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity2,Cual_es_su_preferencia="AREN",Colaborador="manuel",fecha_ingreso =date )
    p1.save()

    return render(request,'principal.html',locals())

     
def crear_colaborador(request):
        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = ColaboradoresForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            temp = form.save(commit=False)
                            temp.fecha_ingreso=datetime.datetime.now()  
                            temp.save() #  

                            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
                            pasword = form.cleaned_data['pasword']
                            correo=form.cleaned_data['email']
                            nom=form.cleaned_data['nombres']
                            apell=form.cleaned_data['apellidos']                            

                            user = User.objects.create_user(username=nombre_de_usuario, password=contracel,email=correo,first_name=nom,last_name=apell)
                            user.save() 

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
            form=ColaboradoresForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 

def crear_usuario(request):
        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = UsuariosForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            temp = form.save(commit=False)
                            temp.fecha_ingreso=datetime.datetime.now()  
                            temp.save() #  

                            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
                            pasword = form.cleaned_data['pasword']
                            correo=form.cleaned_data['email']
                            nom=form.cleaned_data['nombres']
                            apell=form.cleaned_data['apellidos']                            

                            user = User.objects.create_user(username=nombre_de_usuario, password=contracel,email=correo,first_name=nom,last_name=apell)
                            user.save() 

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
            form=UsuariosForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 



def ingresar_datos_de_consulta(request):
        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = Cuestionario_temporalForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            temp = form.save(commit=False)
                            temp.fecha_ingreso=datetime.datetime.now()  
                            temp.Colaborador=request.user.username
                            temp.save() #  
                            
                            Sexoo=form.cleaned_data['Sexo']
                            Rango_de_edadd= form.cleaned_data['Rango_de_edad']
                            Grado_academicoo=form.cleaned_data['Grado_academico']  
                            Estado_socioeconomicoo=form.cleaned_data['Estado_socioeconomico'] 
                            #Departamento_muestraa=form.cleaned_data['Departamento_muestra'] 
                            Ciudad_muestraa=form.cleaned_data['Ciudad_muestra'] 
                            Cual_es_su_preferenciaa=form.cleaned_data['Cual_es_su_preferencia']
                            Colaboradorr=form.cleaned_data['Colaborador']
                            fecha_ingresoo=form.cleaned_data['fecha_ingreso'] 

                            p1=Cuestionario_final(Sexo=Sexoo, Rango_de_edad=Rango_de_edadd, Grado_academico=Grado_academicoo , Estado_socioeconomico=Estado_socioeconomicoo , Ciudad_muestra=Ciudad_muestraa ,Cual_es_su_preferencia=Cual_es_su_preferenciaa ,Colaborador=Colaboradorr ,fecha_ingreso=fecha_ingresoo )
                            p1.save()                            

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
            form=Cuestionario_temporalForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 



def logout(request):
    auth.logout(request)    
    return HttpResponseRedirect("/")

def informacion(request):
  return render(request,'informacion.html',locals())


def principal(request):    
    
    return render(request,'principal.html',locals())

def analisis_de_datos_principal(request):   
    calculo_de_datos()
    
    return render(request,'analisis_de_datos_principal.html',locals())


def grafico_principal(request):   

        datos=Datos_a_graficar.objects.all()

        datosfml=datos.values_list("fml", flat=True)
        datosgan=datos.values_list("gan", flat=True)
        datosvamo=datos.values_list("vamo", flat=True)
        datosalianza=datos.values_list("alianza", flat=True)
        datosaren=datos.values_list("aren", flat=True)
        datospc=datos.values_list("pc", flat=True)
        datospd=datos.values_list("pd", flat=True)
        datosdsv=datos.values_list("dsv", flat=True)                  

        X= np.arange(len(datosfml))
        
        Y1 = np.asarray(datosfml)  
        Y2 = np.asarray(datosgan)
        Y3 = np.asarray(datosvamo)
        Y4 = np.asarray(datosalianza)
        Y5 = np.asarray(datosaren)
        Y6 = np.asarray(datospc)
        Y7 = np.asarray(datosdsv)       
                   
               
        #barh(pos,datos,align = 'center')
        plt.plot(X,Y1, 'r')
        plt.plot(X,Y2, 'c')
        plt.plot(X,Y3, 'b')
        plt.plot(X,Y4, 'p')
        plt.plot(X,Y5, 'b')
        plt.plot(X,Y6, 'g')
        plt.plot(X,Y7, 'o')        
          
        plt.xlabel('Datos de prueba ')
        plt.ylabel('PREFERENCIAS')
        titulo="Tendencia del las preferencias"
        plt.title(titulo)       
               
        subplots_adjust(left=0.21)
      

        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  

        f.clear()
        
        return HttpResponse (buffer.getvalue(), content_type="Image/png")

def calculo_de_datos():
   
        A=Cuestionario_temporal.objects.filter(Sexo="M").count()
        B=Cuestionario_temporal.objects.filter(Sexo="F").count()

        C=Cuestionario_temporal.objects.filter(Rango_de_edad="JOVEN").count()
        D=Cuestionario_temporal.objects.filter(Rango_de_edad="JOVEN_ADULTO").count()
        E=Cuestionario_temporal.objects.filter(Rango_de_edad="ADULTO").count()
        F=Cuestionario_temporal.objects.filter(Rango_de_edad="ADULTO_MAYOR").count()
        G=Cuestionario_temporal.objects.filter(Rango_de_edad="ANCIANO").count()

        H=Cuestionario_temporal.objects.filter(Grado_academico="NO_ESTUDIO").count()
        I=Cuestionario_temporal.objects.filter(Grado_academico="EDUCACION_BASICA").count()
        J=Cuestionario_temporal.objects.filter(Grado_academico="BACHILLERATO").count()
        K=Cuestionario_temporal.objects.filter(Grado_academico="ESTUDIOS_UNIVERSITARIOS").count()
        L=Cuestionario_temporal.objects.filter(Grado_academico="PROFESIONAL").count()

        M=Cuestionario_temporal.objects.filter(Estado_socioeconomico="DESEMPLEADO").count()
        N=Cuestionario_temporal.objects.filter(Estado_socioeconomico="NEGOCIO_PROPIO").count()
        O=Cuestionario_temporal.objects.filter(Estado_socioeconomico="EMPLEADO_PUBLICO").count()
        P=Cuestionario_temporal.objects.filter(Estado_socioeconomico="EMPLEADO_PRIVADO").count()
        Q=Cuestionario_temporal.objects.filter(Estado_socioeconomico="TRABAJO_LA_TIERRA").count()

        R=Cuestionario_temporal.objects.filter(Cual_es_su_preferencia="FML").count()
        S=Cuestionario_temporal.objects.filter(Cual_es_su_preferencia="GAN").count()
        T=Cuestionario_temporal.objects.filter(Cual_es_su_preferencia="VAMO").count()
        U=Cuestionario_temporal.objects.filter(Cual_es_su_preferencia="ALIANZA").count()
        V=Cuestionario_temporal.objects.filter(Cual_es_su_preferencia="AREN").count()
        W=Cuestionario_temporal.objects.filter(Cual_es_su_preferencia="PC").count()
        X=Cuestionario_temporal.objects.filter(Cual_es_su_preferencia="PD").count()
        Y=Cuestionario_temporal.objects.filter(Cual_es_su_preferencia="DSV").count()

        datos_a_sumar=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y]
        
        finales=[]

        try:
            datos=Datos_a_graficar.objects.all().last()        
            for i in range(len(datos)):
                suma=datos_a_sumar[i]+datos[i]
                finales[i]=suma
        except:
            finales=datos_a_sumar


        Cuestionario_temporal.objects.all().delete()
        
        p1=Datos_a_graficar(masculino=finales[0], femenino=finales[1], joven=finales[2],joven_adulto=finales[3], adulto=finales[4],adulto_mayor=finales[5],anciano=finales[6],no_estudio=finales[7],educacion_basica=finales[8],bachillerrato=finales[9],estudios_universitarios=finales[10],profesional=finales[11],desempleado=finales[12],negocio_propio=finales[13],empleado_publico=finales[14],empleado_privado=finales[15],trabajo_la_tierra=finales[16],fml=finales[17],gan=finales[18],vamo=finales[19],alianza=finales[20],aren=finales[21],pc=finales[22],pd=finales[23],dsv=finales[24])
        p1.save()





