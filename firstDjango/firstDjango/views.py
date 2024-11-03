from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("Hello, world! home")
    return render(request , 'website/index.html')

def about(request):
    return HttpResponse("Hello, world! about")

def contact(request):
    return HttpResponse("Hello, world! contact")