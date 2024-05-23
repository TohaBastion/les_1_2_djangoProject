from django.http import HttpResponse
from django.shortcuts import render

def viceversa_home(request):
    return render(request, 'viceversa/home.html')


def reversed(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    num_of_words = len(words)
    reversed_text = user_text[::-1]
    return render(request, 'viceversa/reverse.html', {'usertext': user_text,
                                                      'reversedtext': reversed_text,
                                                      'number_of_words': num_of_words})
