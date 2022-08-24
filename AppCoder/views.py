from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from AppCoder.models import Curso

def inicio(request):
    return HttpResponse("Vista Inicio")

def cursos(request):
    contexto = {
        'cursos' : {
            'curso1': 'Nombre1',
            'curso2': 'Nombre2',
            'curso3': 'Nombre3',
        }
    }
    return render(request, 'cursos.html', contexto)

def profesores(request):
    return render(request, 'profesores.html',)

def estudiantes(request):
    return redirect('AppCoderInicio')

def entregables(request):
    return HttpResponse("Vista Entregables")
