from django.http import HttpResponse


def my_view1(request):
    return HttpResponse('Це другий урок!')


def my_view2(request):
    return HttpResponse('Новий рівень вкладеності')


def my_view3(request):
    return HttpResponse('Нічого собі, ще сторінка!')
