from django.db import models

# Create your models here.

class Employee(models.Model):
    
    employee_name = models.CharField(max_length=55)
    employee_id = models.IntegerField()
    employee_address = models.CharField(max_length=55)
    
    def __str__(self):
        return self.employee_name
    