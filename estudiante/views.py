from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

def estudiantes_curso(request):

    estudiantes = list(Estudiante.objects.values('nombre', 'curso__nombre'))

    return JsonResponse(estudiantes, status=200, safe=False)

def estudiantes_mayores(request, edad):
    estudiantes = list(Estudiante.objects.filter(edad__gt=edad).values('nombre', 'curso__nombre', 'edad'))

    return JsonResponse(estudiantes, status=200, safe=False)
def cursos(request, curso):
    cursos = list(Cursos.objects.filter(nombre=curso).values())

    return JsonResponse(cursos, status=200, safe=False)

def index(request):
    return render(request, 'index.html')
