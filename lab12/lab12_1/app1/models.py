from django.db import models

# Create your models here.
class Factorial(models.Model):
    def calculate(self,num):
        fact = 1
        if num < 0:
            return 0
        for i in range(1, num + 1):
            fact = fact * i
        return fact
    
class OddEven(models.Model):
    def check_Odd_Even(self,num):
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"
