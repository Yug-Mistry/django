from django.shortcuts import render
from app3.models import Job, Book, Customer

# Create your views here.
def show_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'app3/jobs.html', {'jobs':jobs})    

def show_books(request):
    books = Book.objects.all()
    return render(request, 'app3/books.html', {'books':books})

def show_customers(request):
    customer = Customer.objects.all()
    return render(request, 'app3/customers.html', {'customers':customer})    

def insert_job(request, n):
    job = Job()
    job.insertRandomData(n)
    return show_jobs(request)

def insert_book(request, n):
    book = Book()
    book.insertRandomData(n)
    return show_books(request)

def insert_customer(request, n):
    customer = Customer()
    customer.insertRandomData(n)
    return show_customers(request)