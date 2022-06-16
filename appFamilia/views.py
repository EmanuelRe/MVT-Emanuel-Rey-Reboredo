from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import loader
from appFamilia.models import Familia 

# Create your views here.

def familia(self):

    familia1 = Familia(nombre = "Juaquín Perez", parentezco = "hermano", edad = "24", nacimiento = "1998-10-24")
    familia1.save()

    familia2 = Familia(nombre = "Sofía Perez", parentezco = "madre", edad = "55", nacimiento = "1967-11-19")
    familia2.save()

    familia3 = Familia(nombre = "Hernesto Perez", parentezco = "padre", edad = "57", nacimiento = "1965-7-14")
    familia3.save()

    documento = f"Mi primer familiar se llama {familia1.nombre}, es mi {familia1.parentezco}, tiene {familia1.edad} y su fecha de nacimiento es {familia1.nacimiento}, Mi segundo familiar se llama {familia2.nombre}, es mi {familia2.parentezco}, tiene {familia2.edad} y su fecha de nacimiento es {familia2.nacimiento} y mi tercer familiar se llama {familia3.nombre}, es mi {familia3.parentezco}, tiene {familia3.edad} y su fecha de nacimiento es {familia3.nacimiento} "

    return HttpResponse(documento)