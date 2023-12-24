from django.db import models

from random import randint
from datetime import date
from faker import Faker

# Create your models here.
class Job(models.Model):
    date_of_joining = models.DateField()
    location = models.CharField(max_length=50)
    salary = models.IntegerField()
    qualification = models.CharField(max_length=50)
    
    def insertRandomData(self, n=10):        
        fake = Faker()
        for i in range(n):
            Job.objects.create(date_of_joining=date(randint(2000, 2018), randint(1, 12), randint(1, 28)), location=fake.city(), salary=randint(10000, 100000), qualification=fake.job())
    

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date = models.DateField()

    def insertRandomData(self, n=10):
        fake = Faker()
        for i in range(n):
            Book.objects.create(id = self.id,title=fake.sentence(), author=fake.name(), published_date=date(randint(2000, 2018), randint(1, 12), randint(1, 28)))

class Customer(models.Model):
    name = models.CharField(max_length=50)
    ac_no = models.CharField(primary_key=True, max_length=10)
    mailid = models.EmailField()
    phone_number = models.CharField(max_length=10, unique=True)
    age = models.IntegerField()

    def insertRandomData(self, n=10):
        fake = Faker()
        for i in range(n):
            Customer.objects.create(name=fake.name(), ac_no=str(randint(1000000000, 9999999999)), mailid=fake.email(), phone_number=str(randint(1000000000, 9999999999)), age=randint(1, 100))            