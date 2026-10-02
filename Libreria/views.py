from django.shortcuts import HttpResponse

# Create your views here.

def saludos(request):
    return HttpResponse('Hola a todos')

def welcome(request):
    return HttpResponse('Hello everybody')


