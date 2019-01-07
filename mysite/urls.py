#from django.conf.urls import patterns, include, url
#from django.contrib import admin

#from mysite.views import Index

##########################
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url,include

from django.contrib import admin


from django.conf import settings
import mysite.settings

from django.contrib.auth.views import login, logout

from django.conf.urls.static  import static 


from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mysite.views import *
#from histogram import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login,{'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^informacion/$', informacion),
    url(r'^datos_departamento/$', datos_departamento),

    url(r'^crear_colaborador/$', crear_colaborador),
    url(r'^crear_usuario/$', crear_usuario),
    url(r'^ingresar_datos_de_consulta/$', ingresar_datos_de_consulta),

    url(r'^poner_graficos_en _pantalla/$', poner_graficos_en _pantalla),
    url(r'^hacer_calculo_datos/$', hacer_calculo_datos),
    

    
    url(r'^grafico_principal/$', grafico_principal),   
    url(r'^$', principal),

    url(r'^us/$', us),   
    url(r'^cues/$', cues),   
   
      
    

 
       
]

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


