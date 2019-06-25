# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from mi_tienda.models import ClaseA
from mi_tienda.models import Berlinas

# Create your views here.
def home_view (request):
    return render(request, "index.html", {'user':'client'})

def utilitarios_view(request):
    claseA = ClaseA.objects.all()
    return render(request,"ClaseA.html", {'products': claseA})

def berlinas_view(request):
    berlinas = Berlinas.objects.all()
    return render(request,"Berlinas.html", {'products': berlinas})
