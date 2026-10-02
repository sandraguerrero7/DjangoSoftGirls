from django.shortcuts import HttpResponse, render

# Create your views here.

def saludos(request):
    return HttpResponse('Hola a todos')

def welcome(request):
    return HttpResponse('Hello everybody')

def books(request, name=None, author= None):
    if name and author:
         return HttpResponse('Book Name: ' + name + '<br> Author: ' + author)
    elif name:
        return HttpResponse('Book Name: ' + name)
    elif author:
        return HttpResponse('Author: ' + author)
    else:
        return HttpResponse('No book information provided.')


def library(request):
    return render(request, 'general/index.html')

def list(request):
    return render(request, 'libros/catalogo.html')



