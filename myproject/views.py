from django.http import JsonResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles(request, year: int):
    idade = 2022 - year

    return JsonResponse({
        'ano': year,
        'idade': idade,
    })

def ler_do_banco(nome):
    lista_nomes = [
        {'nome': 'Pedro', 'idade': 20},
        {'nome': 'Jose', 'idade': 30},
        {'nome': 'Joao', 'idade': 45},
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0}

def fname(request, nome: str):
    result: dict = ler_do_banco(nome)
    
    if result['idade'] > 0:
        return JsonResponse({
            'Encontrado': True,
            'Name': result['nome'],
            'Idade': result['idade'],
        })
    else:
        return JsonResponse({
            'Encontrado': 'False',
        })