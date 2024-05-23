from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello!')


def index_2024(request):
    return HttpResponse('2024')


def index_name(request):
    return HttpResponse('Anton')
