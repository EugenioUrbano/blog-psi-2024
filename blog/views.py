from django.shortcuts import render
from .models import Genero, Post

def index(request):
    posts = Post.objects.all()

    context = {
        "Posts": posts,
    }
    return render(request, 'index.html', context)

def genero(request):
    generos = Genero.objects.all()

    context = {
        "Generos": generos,
    }
    return render(request, 'genero.html', context)

