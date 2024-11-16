from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.

def all_test(request):
    chais = ChaiVarity.objects.all()
    return render(request , 'tester/all_test.html',{'chais' : chais})
