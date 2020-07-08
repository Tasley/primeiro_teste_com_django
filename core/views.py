from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Teste primeiro App web com Django. Bem vindo {}. Voce tem {} anos.</h1>'.format(nome, idade))

def somar (request, valor_1, valor_2):
    return HttpResponse('A soma dos valores {} e {} e igual a: {}'.format(valor_1, valor_2,valor_1 +valor_2))

def subtrair (request, valor_1, valor_2):
    return HttpResponse('A subtracao dos valores {} e {} e igual a: {}'.format(valor_1, valor_2,valor_1 - valor_2))

def multiplicar (request, valor_1, valor_2):
    return HttpResponse('A multiplicacao dos valores {} e {} e igual a: {}'.format(valor_1, valor_2,valor_1 * valor_2))

def dividir (request, valor_1, valor_2):
    return HttpResponse('A divisao dos valores {} e {} e igual a: {}'.format(valor_1, valor_2,valor_1 / valor_2))

def resto (request, valor_1, valor_2):
    return HttpResponse('O resto da divisao de {} por {} e igual a: {}'.format(valor_1, valor_2,valor_1 % valor_2))