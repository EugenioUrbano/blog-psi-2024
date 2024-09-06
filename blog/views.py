from django.shortcuts import render
from .models import Genero

def index(request):
    generos = Genero.objects.all()

    context = {
        "Generos": generos,
    }
    return render(request, 'index.html', context)

