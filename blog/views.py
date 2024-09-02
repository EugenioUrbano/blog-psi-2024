from django.shortcuts import render

def index(request):
    generos= {"titulo": "titulo" }
    return render(request, 'index.html')