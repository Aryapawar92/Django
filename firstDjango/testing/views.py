from django.shortcuts import render

# Create your views here.

def all_test(request):
    return render(request , 'tester/all_test.html')