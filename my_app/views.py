from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#MVC - Django
# M - models.py
# V - é o html
# C - views.py

#MTV
# M - models.py
# T - template
# V - views.py

def home(request):
    return HttpResponse('Olá mundo!')

def home_param(request, post_id):
    return HttpResponse('Olá mundo!! %s' % post_id)