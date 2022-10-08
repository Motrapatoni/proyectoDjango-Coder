from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime, timedelta

from home.models import Persona

def hola(request):
    return HttpResponse('<h1>Esto es nuevo</h1>')

def dia_de_hoy(request):
    dia = datetime.now()
    doc = f'Hoy es: <br> {dia}'
    return HttpResponse(doc)

def nombre(request, nombre):
    doc = f'Mi nombre es: <br><h2>{nombre}</h2>'
    return HttpResponse(doc)

def vista_template(request):
    temp = open(r'/Users/moises.ramirez/Desktop/Dev/python/Python-Coder/Coder-Django/DjangoProject1/templates/template1.html', 'r')
    plantilla = Template(temp.read())
    temp.close()
    cont = Context()
    doc = plantilla.render(cont)
    return HttpResponse(doc)

def post_person(request, name, lastname, email):
    
    persona = Persona(nombre=name, apellido=lastname, edad=datetime.now(), mail=email)
    persona.save()
    template = loader.get_template('post_user.html')
    document = template.render({'persona': persona})
    return HttpResponse(document)

def get_persons(request):

    personas = Persona.objects.all()
    
    template = loader.get_template('get_user.html')
    tem_render = template.render({'persona': personas})
    return HttpResponse(tem_render)