from django.http import JsonResponse

def hello(request):
    return JsonResponse({
        'nome': "Pedro",
    })

def articles(request, year):
    return JsonResponse({
        'ano': str(year)
    })