from contextvars import Context
from pipes import Template
from django.http import HttpResponse
from datetime import datetime
from django.template import Template
from django.template import Context

def saludo(request):
    return HttpResponse("Hola Django - puto de mierda") 

def fechaa(request):
    dia= datetime.now()
    texto = f"Hoy es: <br>,{dia}"
    return HttpResponse(texto)

def parametro(self, nombre):
    texto1 = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(texto1)

def pruebotemplate(self):

    mihtml = open("C:/Users/guido/Documents/Coderhouse/Proyecto1/Proyecto1/Plantilla/Template.html")
    plantila = Template(mihtml.read())
    mihtml.close()
    micontexto = Context()
    documento = plantila.render(micontexto)
    
    return HttpResponse(documento)