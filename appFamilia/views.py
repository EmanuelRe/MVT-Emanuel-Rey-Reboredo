from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import loader
from appFamilia.models import Familia 

# Create your views here.

def familia(request):

    familia1 = Familia(nombre = "Juaquín Perez", parentezco = "hermano", edad = "24", nacimiento = "1998-10-24")
    familia1.save()

    familia2 = Familia(nombre = "Sofía Perez", parentezco = "madre", edad = "55", nacimiento = "1967-11-19")
    familia2.save()

    familia3 = Familia(nombre = "Hernesto Perez", parentezco = "padre", edad = "57", nacimiento = "1965-7-14")
    familia3.save()

    familia = Familia.objects.all()

    ctx = {"familia": familia}
    return render(request, "index.html", ctx)