from django.shortcuts import render
from models import Genero

def index(request):
    context = Genero.objects.all()
    return render(request, 'index.html', context)