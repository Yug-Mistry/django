from django.shortcuts import render
from app1.models import Factorial, OddEven

# Create your views here.
def welcome(request):
    return render(request, 'app1/welcome.html')

def about(request):
    return render(request, 'app1/about.html')

def welcome1(request, usname):
    return render(request, 'app1/welcome1.html', {'usname': usname})

def factorial_view(request,n):
    obj = Factorial()
    fact = obj.calculate(num = n)
    return render(request, 'app1/factorial.html', {'num':n,'fact': fact})

def odd_even_view(request,n):
    obj = OddEven()
    result = obj.check_Odd_Even(num = n)
    return render(request, 'app1/odd_even.html', {'num':n,'result': result})
