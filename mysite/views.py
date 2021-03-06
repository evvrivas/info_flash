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


def datos_departamento(request,contra):
        if contra=="ecopes":
            depto="AHUACHAPAN"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Ahuachapán","Apaneca","Atiquizaya","Concepción de Ataco","El Refugio","Guaymango","Jujutla","San Francisco Menéndez","San Lorenzo","San Pedro Puxtla","Turín","Tacuba"]
            ciudades=["Ahuachapán"]
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()


            depto="SANTA ANA"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Candelaria de la Frontera","Chalchuapa","Coatepeque","El Congo","El Porvenir","Masahuat","Metapán","San Antonio Pajonal","San Sebastián Salitrillo","Santa Ana","Santa Rosa Guachipilín","Santiago de la Frontera","Texistepeque"]
            ciudades=["Santa Ana"]
            
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()


            depto="SONSONATE"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Acajutla","Armenia","Caluco","Cuisnahuat","Izalco","Juayúa","Nahuizalco","Nahulingo","Salcoatitán","San Antonio del Monte","San Julián","Santa Catarina Masahuat","Santa Isabel Ishuatán","Santo Domingo Guzmán","Sonsonate","Sonzacate"]
            ciudades=["Sonsonate"]
           
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()


            depto="CHALATENANGO"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Agua Caliente","Arcatao","Azacualpa","Chalatenango","Comalapa","Citalá","Concepción Quezaltepeque","Dulce Nombre de María","El Carrizal","El Paraíso","La Laguna","La Palma","La Reina","Las Vueltas","Nueva Concepción","Nueva Trinidad","Nombre de Jesús","Ojos de Agua","Potonico","San Antonio de la Cruz","San Antonio Los Ranchos","San Fernando","San Francisco Lempa","San Francisco Morazán","San Ignacio","San Isidro Labrador","San José Cancasque","San José Las Flores","San Luis del Carmen","San Miguel de Mercedes","San Rafael","Santa Rita","Tejutla"]
            ciudades=["Chalatenango"]
          
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()


            depto="CUSCATLAN"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Candelaria","Cojutepeque","El Carmen","El Rosario","Monte San Juan","Oratorio de Concepción","San Bartolomé Perulapía","San Cristóbal","San José Guayabal","San Pedro Perulapán","San Rafael Cedros","San Ramón","Santa Cruz Analquito","Santa Cruz Michapa","Suchitoto","Tenancingo"]
            ciudades=["Cuscatlan"]
           
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()


            depto="SAN SALVADOR"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Aguilares","Apopa","Ayutuxtepeque","Cuscatancingo","Ciudad Delgado","El Paisnal","Guazapa","Ilopango","Mejicanos","Nejapa","Panchimalco","Rosario de Mora","San Marcos","San Martín","San Salvador","Santiago Texacuangos","Santo Tomás","Soyapango","Tonacatepeque"]
            ciudades=["San Salvador"]
            
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()
              


            depto="LA LIBERTAD"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Antiguo Cuscatlán","Chiltiupán","Ciudad Arce","Colón","Comasagua","Huizúcar","Jayaque","Jicalapa","La Libertad","Santa Tecla","Nuevo Cuscatlán","San Juan Opico","Quezaltepeque","Sacacoyo","San José Villanueva","San Matías","San Pablo Tacachico","Talnique","Tamanique","Teotepeque","Tepecoyo","Zaragoza"]
            ciudades=["La Libertad"]
           
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()


            depto="SAN VICENTE"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Apastepeque","Guadalupe","San Cayetano Istepeque","San Esteban Catarina","San Ildefonso","San Lorenzo","San Sebastián","San Vicente","Santa Clara","Santo Domingo","Tecoluca","Tepetitán","Verapaz"]
            ciudades=["San Vicente"]
           
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()

            depto="CABANAS"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Cinquera","Dolores","Guacotecti","Ilobasco","Jutiapa","San Isidro","Sensuntepeque","Tejutepeque","Victoria"]
            ciudades=["Cabanas"]
           
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()

            depto="LA PAZ"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Cuyultitán","El Rosario","Jerusalén","Mercedes La Ceiba","Olocuilta","Paraíso de Osorio","San Antonio Masahuat","San Emigdio","San Francisco Chinameca","San Juan Nonualco","San Juan Talpa","San Juan Tepezontes","San Luis Talpa","San Luis La Herradura","San Miguel Tepezontes","San Pedro Masahuat","San Pedro Nonualco","San Rafael Obrajuelo","Santa María Ostuma","Santiago Nonualco","Tapalhuaca","Zacatecoluca"]
            ciudades=["La Paz"]
           
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()

            depto="USULUTAN"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Alegría","Berlín","California","Concepción Batres","El Triunfo","Ereguayquín","Estanzuelas","Jiquilisco","Jucuapa","Jucuarán","Mercedes Umaña","Nueva Granada","Ozatlán","Puerto El Triunfo","San Agustín","San Buenaventura","San Dionisio","San Francisco Javier","Santa Elena","Santa María","Santiago de María","Tecapán","Usulután"]
            ciudades=["Usulután"]
           
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()

            depto="SAN MIGUEL"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Carolina","Chapeltique","Chinameca","Chirilagua","Ciudad Barrios","Comacarán","El Tránsito","Lolotique","Moncagua","Nueva Guadalupe","Nuevo Edén de San Juan","Quelepa","San Antonio del Mosco","San Gerardo","San Jorge","San Luis de la Reina","San Miguel","San Rafael Oriente","Sesori","Uluazapa"]
            ciudades=["San Miguel"]
           
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()


            depto="MORAZAN"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Arambala","Cacaopera","Chilanga","Corinto","Delicias de Concepción","El Divisadero","El Rosario","Gualococti","Guatajiagua","Joateca","Jocoaitique","Jocoro","Lolotiquillo","Meanguera","Osicala","Perquín","San Carlos","San Fernando","San Francisco Gotera","San Isidro","San Simón","Sensembra","Sociedad","Torola","Yamabal","Yoloaiquín"]
            ciudades=["Morazan"]
            
            for i in ciudades:
                p2=Ciudades(departamento=p1,nombre=i)
                p2.save()


            depto="LA UNION"    
            p1=Departamentos(nombre=depto)   
            p1.save() 
            #ciudades=["Anamorós","Bolivar","Concepción de Oriente","Conchagua","El Carmen","El Sauce","Intipucá","La Unión","Lislique","Meanguera del Golfo","Nueva Esparta","Pasaquina","Polorós","San Alejo","San José","Santa Rosa de Lima","Yayantique","Yucuaiquín"]
            ciudades=["La Unión"]
           
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




import random
def cues(request):  


    sity=Ciudades.objects.get(id=1)
    sity2=Ciudades.objects.get(id=4)
    date=datetime.datetime.now()  
    
    
    selec=['FML','GAN','VAMO','AREN','PC','PD','DSV','NS/NR']
    
    i=random.randrange(0, 8)
    p1=Cuestionario_temporal(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_final(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()


    i=random.randrange(0, 8)
    p1=Cuestionario_temporal(Sexo="F",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity2,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_final(Sexo="F",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity2,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    
    
    i=random.randrange(0, 8)
    p1=Cuestionario_temporal(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_final(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()

   

    i=random.randrange(0, 8)
    p1=Cuestionario_temporal(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity2,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_final(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity2,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
       

    i=random.randrange(0, 8)
    p1=Cuestionario_temporal(Sexo="F",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_final(Sexo="F",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()


    i=random.randrange(0, 8)
    p1=Cuestionario_temporal(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_final(Sexo="M",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
   

    i=random.randrange(0, 8)
    p1=Cuestionario_temporal(Sexo="F",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity2,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
    p1=Cuestionario_final(Sexo="F",Rango_de_edad="JOVEN_ADULTO", Grado_academico="BACHILLERATO",Estado_socioeconomico="EMPLEADO_PUBLICO",  Ciudad_muestra=sity2,Cual_es_su_preferencia=selec[i],Colaborador="manuel",fecha_ingreso =date )
    p1.save()
   

    return render(request,'principal.html',locals())

     
def crear_colaborador(request):

        departamentos=Departamentos.objects.all()



        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = ColaboradoresForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            temp = form.save(commit=False)
                            temp.fecha_ingreso=datetime.datetime.now()  
                            temp.save() #  

                            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
                            contra = form.cleaned_data['pasword']
                            correo=form.cleaned_data['email']
                            nom=form.cleaned_data['nombres']
                            apell=form.cleaned_data['apellidos']  


                            user2 = User.objects.filter(username=nombre_de_usuario).exists()

                            if user2==False:                           

                                    user = User.objects.create_user(username=nombre_de_usuario, password=contra,email=correo,first_name=nom,last_name=apell)
                                    user.save() 

                                    form.save() # Guardar los datos en la base de datos  print 
                                    #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                                    connection.close()
                                    return render(request,'confirmar.html',locals())                  
                            else:
                                memnsaje="El usuario ya existe, intente con otro usuario"
                                form=UsuariosForm()
                                connection.close()                  
                                return render(request,'ingreso_de_datos.html',locals())
    

        else:            
                         
            form=ColaboradoresForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 

def crear_usuario(request):
        departamentos=Departamentos.objects.all()
        import os, sys
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                             
                    form = UsuariosForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :
                           
                            temp = form.save(commit=False)
                            temp.fecha_ingreso=datetime.datetime.now()  
                            temp.save() #  

                            nombre_de_usuarioo = form.cleaned_data['nombre_de_usuario']
                            contraa = form.cleaned_data['pasword']
                            correoo=form.cleaned_data['email']
                            nomm=form.cleaned_data['nombres']
                            apelll=form.cleaned_data['apellidos'] 

                            user2 = User.objects.filter(username=nombre_de_usuarioo).exists()

                            if user2==False:    
                                    user = User.objects.create_user(username=nombre_de_usuarioo, password=contraa,email=correoo,first_name=nomm,last_name=apelll)
                                    user.save() 

                                    form.save() # Guardar los datos en la base de datos  print 
                                    #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                                    connection.close()
                                    return render(request,'confirmar.html',locals())                  
                            else:
                                memnsaje="El usuario ya existe, intente con otro usuario"
                                form=UsuariosForm()
                                connection.close()                  
                                return render(request,'ingreso_de_datos.html',locals())

        else:            
                         
            form=UsuariosForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 


@login_required
def ingresar_datos_de_consulta(request):
    import os, sys
    departamentos=Departamentos.objects.all()
    

    
    colaboradorr=Colaboradores.objects.filter(nombre_de_usuario=request.user.username).first()
                      
           
    if colaboradorr.estado_colaborador=="DE_ALTA":
                bandera=1
    else:
                bandera=0

    if bandera==1:
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
                            Departamento_muestraa=form.cleaned_data['Departamento_muestra'] 
                            Ciudad_muestraa=form.cleaned_data['Ciudad_muestra'] 
                            Cual_es_su_preferenciaa=form.cleaned_data['Cual_es_su_preferencia']
                            Colaboradorr=request.user.username
                            #fecha_ingresoo=form.cleaned_data['fecha_ingreso'] 
                            fecha_ingresoo=datetime.datetime.now()  
                            p1=Cuestionario_final(Sexo=Sexoo, Rango_de_edad=Rango_de_edadd, Grado_academico=Grado_academicoo , Estado_socioeconomico=Estado_socioeconomicoo ,Departamento_muestra=Departamento_muestraa, Ciudad_muestra=Ciudad_muestraa ,Cual_es_su_preferencia=Cual_es_su_preferenciaa ,Colaborador=Colaboradorr ,fecha_ingreso=fecha_ingresoo )
                            p1.save()                            

                            form.save() # Guardar los datos en la base de datos  print 
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
            form=Cuestionario_temporalForm()

        connection.close()                  
        return render(request,'ingreso_de_datos.html',locals()) 
    else:
        return render(request,'principal.html',locals()) 

def logout(request):
    auth.logout(request)    
    return HttpResponseRedirect("/")

def informacion(request):
  departamentos=Departamentos.objects.all()
  return render(request,'informacion.html',locals())


def principal(request):
    departamentos=Departamentos.objects.all()
    configurar=Configuracion_sistema.objects.all().first()
    configurar.n_visitas+=1         
    configurar.save()
    
    return render(request,'principal.html',locals())

@login_required
def poner_graficos_en_pantalla(request,bandera):    
    departamentos=Departamentos.objects.all()

    usuarioo=Usuarios.objects.filter(nombre_de_usuario=request.user.username).first()
                      
           
    if usuarioo.estado_del_plan!="DE_ALTA":
                bandera=3


    return render(request,'analisis_de_datos_principal.html',locals())


def hacer_calculo_datos(request):
    departamentos=Departamentos.objects.all()   
    calculo_de_datos()
    
    return render(request,'principal.html',locals())

@login_required
def tabular_datos(request):   
    departamentos=Departamentos.objects.all()
    datos=Datos_a_graficar.objects.all()   
    datos_crudos=Cuestionario_final.objects.all()
    return render(request,'tablas.html',locals())

@login_required
def grafico_de_barras_principal(request):
        departamentos=Departamentos.objects.all() 

        usuarioo=Usuarios.objects.filter(nombre_de_usuario=request.user.username).first()
        
        datos=Datos_a_graficar.objects.all().order_by("-id")[0]    
        
        aa=datos.aren+datos.pc+datos.pd+datos.dsv

        total=datos.fml+datos.gan+datos.vamo+datos.aren+datos.pc+datos.pd+datos.dsv+datos.ns_nr
       
        fml=round(datos.fml*100/total,2)
        gan=round(datos.gan*100/total,2)
        vamo=round(datos.vamo*100/total,2)
        aaa=round(aa*100/total,2)
        aren=round(datos.aren*100/total,2)
        pc=round(datos.pc*100/total,2)
        pd=round(datos.pd*100/total,2)
        dsv=round(datos.dsv*100/total,2)
        ns_nr=round(datos.ns_nr*100/total,2)     

        datos2=[fml,gan,vamo,aaa,ns_nr,0,0,aren,pc,pd,dsv] 
       
        nombre=[]
        valor=[]


        for i in datos2:
            nombre.append(i)
            

        X= np.arange(len(datos2))
        
        Y1 = np.asarray(datos2)  
                       
               
        f=plt.figure()
       
            
        bar_width = 0.45
        plt.bar(X, Y1, bar_width, color='b')
        
        SIMBOLO_G=["fml","gan","vamo","alian","NS/NR","-","-","aren","pc","pd","dsv"]
      
        z=0 
        for x, y in zip(X, Y1):
            plt.text(x, y+1 ,str(y)+ "\n"+SIMBOLO_G[z], ha='center', va= 'bottom')
            z=z+1
 
      
        plt.xlabel(' participantes del estudio ')
        plt.ylabel('preferencias ')
        titulo="RESULTADO NACIONAL"
        plt.title(titulo)
        plt.xticks(())

        subplots_adjust(left=0.21)
      

        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  

        f.clear()
        
        return HttpResponse (buffer.getvalue(), content_type="Image/png")

@login_required
def grafico_de_tendencia_principal(request):   

        
        datos=Datos_a_graficar.objects.order_by('-id')[0]
        aa=datos.aren+datos.pc+datos.pd+datos.dsv
      
        total=datos.masculino+datos.femenino        
        pfml = round(datos.fml*100/total,2)
        pgan = round(datos.gan*100/total,2)
        pvamo = round(datos.vamo*100/total,2)
        paa = round(aa*100/total,2)        
        pns_nr = round(datos.dsv*100/total,2)



        datos=Datos_a_graficar.objects.all()

        datosfml=datos.values_list("fml", flat=True)
        datosgan=datos.values_list("gan", flat=True)
        datosvamo=datos.values_list("vamo", flat=True)
        datosalianza=datos.values_list("alianza", flat=True)
        datosaren=datos.values_list("aren", flat=True)
        datospc=datos.values_list("pc", flat=True)
        datospd=datos.values_list("pd", flat=True)
        datosdsv=datos.values_list("dsv", flat=True)   
        datosns_nr=datos.values_list("ns_nr", flat=True)  

        

        X= np.arange(len(datosfml))
        
        Y1 = np.asarray(datosfml)  
        Y2 = np.asarray(datosgan)
        Y3 = np.asarray(datosvamo)
        Y4 = np.asarray(datosalianza)
        Y5 = np.asarray(datosaren)
        Y6 = np.asarray(datospc)
        Y7 = np.asarray(datospd)        
        Y8 = np.asarray(datosdsv)   
        Y9 = np.asarray(datosns_nr) 


               
        #barh(pos,datos,align = 'center')
        f=plt.figure()
        plt.plot(X,Y1, 'red')
        plt.plot(X,Y2, 'aqua')
        plt.plot(X,Y3, 'darkblue')
        plt.plot(X,Y4, 'gray')   

        plt.plot(X,Y8, 'black')     

        plt.grid()     
        

        leyenda="rojo=fml "+str(pfml)+ "%        aqua=gan "+str(pgan)+   "%    azul=vam "+str(pvamo)+   "%    gris=alianza "+str(paa)+  "%    negro=NS/NR "+str(pns_nr)
        plt.xlabel(leyenda)
           
        plt.ylabel('PREFERENCIAS')
        titulo="Tendencia del las preferencias"
        plt.xticks(())
        plt.yticks(())
      
        #titulo="Tendencia del las preferencias\n"+" fml "+str(fml)+ "%    "+  "gan "+str(gan)+ "%    "+"vamo "+str(vamo)+ "%    "+"alian "+str(aaa)+ "%" +  "NS+NR "+str(ns_nr)+ "%"
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
        Z=Cuestionario_temporal.objects.filter(Cual_es_su_preferencia="NS/NR").count()

        U=V+W+X+Y
        
        datos_a_sumar=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
        
        finales=[]

        datos=Datos_a_graficar.objects.order_by('-id')[0]

        aa=datos.aren+datos.pc+datos.pd+datos.dsv

        datos2=[datos.masculino, datos.femenino, datos.joven, datos.joven_adulto,datos.adulto,datos.adulto_mayor,datos.anciano,datos.no_estudio,datos.educacion_basica,datos.bachillerrato,datos.estudios_universitarios,datos.profesional,datos.desempleado,datos.negocio_propio,datos.empleado_publico,datos.empleado_privado,datos.trabajo_la_tierra,datos.fml,datos.gan,datos.vamo,aa,datos.aren,datos.pc,datos.pd,datos.dsv,datos.ns_nr]      
        
        for i in range(len(datos_a_sumar)):
            suma=datos_a_sumar[i]+datos2[i]
            finales.append(suma)


        Cuestionario_temporal.objects.all().delete()
        
        p1=Datos_a_graficar(masculino=finales[0], femenino=finales[1], joven=finales[2],joven_adulto=finales[3], adulto=finales[4],adulto_mayor=finales[5],anciano=finales[6],no_estudio=finales[7],educacion_basica=finales[8],bachillerrato=finales[9],estudios_universitarios=finales[10],profesional=finales[11],desempleado=finales[12],negocio_propio=finales[13],empleado_publico=finales[14],empleado_privado=finales[15],trabajo_la_tierra=finales[16],fml=finales[17],gan=finales[18],vamo=finales[19],alianza=finales[20],aren=finales[21],pc=finales[22],pd=finales[23],dsv=finales[24],ns_nr=finales[25])
        p1.save()



@login_required
def datos_generales(request):
    departamentos=Departamentos.objects.all()
    datos=Datos_a_graficar.objects.order_by('-id')[0]
    aa=datos.aren+datos.pc+datos.pd+datos.dsv
    datos2=[datos.masculino, datos.femenino, datos.joven, datos.joven_adulto,datos.adulto,datos.adulto_mayor,datos.anciano,datos.no_estudio,datos.educacion_basica,datos.bachillerrato,datos.estudios_universitarios,datos.profesional,datos.desempleado,datos.negocio_propio,datos.empleado_publico,datos.empleado_privado,datos.trabajo_la_tierra,datos.fml,datos.gan,datos.vamo,aa,datos.aren,datos.pc,datos.pd,datos.dsv,datos.ns_nr]      
    
    total=datos.masculino+datos.femenino

    femenino=round(datos.femenino*100/total,2)
    masculino=round(datos.masculino*100/total,2)
    
    joven = round(datos.joven*100/total ,2)
    joven_adulto = round(datos.joven_adulto*100/total,2)
    adulto = round(datos.adulto*100/total,2)
    adulto_mayor = round(datos.adulto_mayor*100/total,2)
    anciano = round(datos.anciano*100/total,2)

    no_estudio = round(datos.no_estudio*100/total,2)
    educacion_basica = round(datos.educacion_basica*100/total,2)
    bachillerrato = round(datos.bachillerrato*100/total,2)
    estudios_universitarios = round(datos.estudios_universitarios*100/total,2)
    profesional = round(datos.profesional*100/total,2)

    desempleado = round(datos.desempleado*100/total,2)
    negocio_propio = round(datos.negocio_propio*100/total,2)
    empleado_publico = round(datos.empleado_publico*100/total,2)
    empleado_privado = round(datos.empleado_privado*100/total,2)
    trabajo_la_tierra = round(datos.trabajo_la_tierra*100/total,2)

    fml = round(datos.fml*100/total,2)
    gan = round(datos.gan*100/total,2)
    vamo = round(datos.vamo*100/total,2)
    aren = round(datos.aren*100/total,2)
    pc = round(datos.pc*100/total,2)
    pd = round(datos.pd*100/total,2)
    dsv = round(datos.dsv*100/total,2)
    ns_nr = round(datos.dsv*100/total,2)

    return render(request,'datos_generales.html',locals())

def departamental(request,depto):
    departamentos=Departamentos.objects.all()
    usuarioo=Usuarios.objects.filter(nombre_de_usuario=request.user.username).first()
    return render(request,'departamentales.html',locals())



@login_required
def cruce_de_datos(request,depto):
        datos1=Cuestionario_final.objects.filter(Q(Ciudad_muestra__departamento__nombre=depto) & Q(Cual_es_su_preferencia__contains="FML")).count()
        datos2=Cuestionario_final.objects.filter(Q(Ciudad_muestra__departamento__nombre=depto) & Q(Cual_es_su_preferencia__contains="GAN")).count()
        datos3=Cuestionario_final.objects.filter(Q(Ciudad_muestra__departamento__nombre=depto) & Q(Cual_es_su_preferencia__contains="VAMO")).count()
        
        datos4=Cuestionario_final.objects.filter(Q(Ciudad_muestra__departamento__nombre=depto) & Q(Cual_es_su_preferencia__contains="AREN")).count()
        datos5=Cuestionario_final.objects.filter(Q(Ciudad_muestra__departamento__nombre=depto) & Q(Cual_es_su_preferencia__contains="PC")).count()
        datos6=Cuestionario_final.objects.filter(Q(Ciudad_muestra__departamento__nombre=depto) & Q(Cual_es_su_preferencia__contains="PD")).count()
        datos7=Cuestionario_final.objects.filter(Q(Ciudad_muestra__departamento__nombre=depto) & Q(Cual_es_su_preferencia__contains="DSV")).count()
        
        datos8=Cuestionario_final.objects.filter(Q(Ciudad_muestra__departamento__nombre=depto) & Q(Cual_es_su_preferencia__contains="NS/NR")).count()
    
        aa=datos4+datos5+datos6+datos7
        #datos2=[datos1,datos2,datos3,aa,datos4,datos5,datos6,datos7,datos8] 
        
        #datos1  fml
        #datos2  gan
        #datos3  vamo
        #aa  aa
        #datos4  aren
        #datos5  pc
        #datos6  pd
        #datos7 dsv
        #datos8 ns_nr


        total=datos1+datos2+datos3+datos8+aa
       
        fml=round(datos1*100/total,2)
        gan=round(datos2*100/total,2)
        vamo=round(datos3*100/total,2)
        aaa=round(aa*100/total,2)
        aren=round(datos4*100/total,2)
        pc=round(datos5*100/total,2)
        pd=round(datos6*100/total,2)
        dsv=round(datos7*100/total,2)
        ns_nr=round(datos8*100/total,2)     

        datos2=[fml,gan,vamo,aaa, ns_nr,0,0, aren,pc,pd,dsv,] 
       
        nombre=[]
        valor=[]


        for i in datos2:
            nombre.append(i)
            

        X= np.arange(len(datos2))
        
        Y1 = np.asarray(datos2)  
                       
               
        f=plt.figure()
       
            
        bar_width = 0.45
        plt.bar(X, Y1, bar_width, color='b')
        
        SIMBOLO_G=["fml","gan","vamo","alian","NS/NR","-","-","aren","pc","pd","dsv"]
      
        z=0 
        for x, y in zip(X, Y1):
            plt.text(x, y+1 ,str(y)+ "\n"+SIMBOLO_G[z], ha='center', va= 'bottom')
            z=z+1
 
      
        plt.xlabel(' participantes del estudio ')
        plt.ylabel('preferencias ')
        titulo=depto
        plt.title(titulo)
        plt.xticks(())

        subplots_adjust(left=0.21)
      

        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  

        f.clear()
        
        return HttpResponse (buffer.getvalue(), content_type="Image/png")




        