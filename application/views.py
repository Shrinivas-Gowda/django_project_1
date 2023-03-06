from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Sample(request):
    return HttpResponse('<marquee><h1>Hello World how are you<h1></marquee>')

def Sample1(request):
    return HttpResponse('azqwxsecdrfvtgbyhnumi,o')
