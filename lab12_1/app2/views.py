from django.shortcuts import render
from app2.models import Employee

# Create your views here.
def show_employees(request):
    employees = Employee.objects.all()
    return render(request, 'app2/showEmployees.html', {'employees':employees})