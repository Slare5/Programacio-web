from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import *
from datos.models import Tipo, Subcategoria, Lenguaje

# Create your views here.
def index(request):
    template = loader.get_template('prueba/index.html')
    return HttpResponse(template.render())

def encuesta(request, id_ronda):
    id_ronda = int(id_ronda)

    if id_ronda == 0:
        varname = 'tipoLenguaje'
        datos = Tipo.objects.all()
    elif id_ronda == 1:
        try:
            varname = 'id'
            req_tipo = Tipo.objects.get(id = request.GET['tipoLenguaje'])
            datos = Subcategoria.objects.filter(foranea_tipo = req_tipo).order_by('?')
        except Exception, e:
            datos = []

    template = loader.get_template('prueba/encuesta.html')
    context = RequestContext(request, {
        'datos': datos,
        'ronda': id_ronda,
        'formname': varname,
        'siguiente_ronda': id_ronda+1,
    })
    return HttpResponse(template.render(context))

def resultado(request):
    try:
        subcat = Subcategoria.objects.get(id = request.GET['id'])
        resultado = Lenguaje.objects.filter(foranea_subcat = subcat )
    except Exception, e:
        resultado = []

    template = loader.get_template('prueba/resultado.html')
    context = RequestContext(request, {
        'resultados': resultado
    })
    return HttpResponse(template.render(context))