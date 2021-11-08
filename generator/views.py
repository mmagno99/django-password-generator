from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijkmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^_-&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))


    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'password.html', {'password':generated_password})