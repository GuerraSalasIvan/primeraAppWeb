from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render (request, 'blog/index.html')

def animal_list(request):
    animales = Animal.objects.all()
    return render(request, 'blog/animal_list.html', {'animales_mostrar': animales})

def colaborador_list(request):
    colaborador = Colaborador.objects.all()
    return render(request, 'blog/colaborador_list.html',{'colaboradores_mostrar':colaborador})

def protectora_list(request):
    protectora = Protectora.objects.all()
    return render(request, 'blog/protectora_list.html',{'protectoras_mostrar':protectora})