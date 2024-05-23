from django.http import HttpResponse


def home(request):
    return HttpResponse('Home!')


def about(request):
    return HttpResponse('about')


def contact(request):
    return HttpResponse('contact')


def profile(request, username):
    return HttpResponse(f'Hello {username}')
