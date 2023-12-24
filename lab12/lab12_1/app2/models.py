from django.db import models

# Create your models here.
class Employee(models.Model):
    id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=255) 

    def __str__(self):
        return " ID:"+str(self.id)+"Name:"+self.name+" Address:"+self.address
    
    class Meta:
        db_table = 'Customers'
       