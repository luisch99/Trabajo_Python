from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from AppLuis.models import Familia
# Create your views here.

def fami(self):
    familiar=Familia(nombre="Luis",apellido="Chuquichanca",tlf=960224122,fechaNac="1999-05-08")
    familiar2=Familia(nombre="Godofredo",apellido="Chuquichanca",tlf=983823211,fechaNac="1960-05-20")
    familiar3=Familia(nombre="Edith",apellido="Cañari",tlf=983343211,fechaNac="1972-05-30")

    texto=f"Familiar creado: {familiar.nombre} {familiar.apellido} {familiar.tlf} {familiar.fechaNac}"
    texto2=f"Familiar creado: {familiar2.nombre} {familiar2.apellido} {familiar2.tlf} {familiar2.fechaNac}"
    texto3=f"Familiar creado: {familiar3.nombre} {familiar3.apellido} {familiar3.tlf} {familiar3.fechaNac}"
    return HttpResponse(texto+"<br>"+texto2+"<br>"+texto3)