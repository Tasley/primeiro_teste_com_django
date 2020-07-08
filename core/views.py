from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Teste primeiro App web com Django. Bem vindo {}. Voce tem {} anos.</h1>'.format(nome, idade))