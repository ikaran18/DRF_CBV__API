from django.db import models

# Create your models here.

WORK_CHOICES = (
    ('Software','Software'),
    ('Service','Service'),
    ('Digital Marketing','Digital Marketing'),
    ('BPO Calling','BPO Calling'),
)


class Company(models.Model):
    
    company_name = models.CharField(max_length=55)
    company_work = models.CharField( choices=WORK_CHOICES , max_length=55)
    company_id = models.CharField(max_length=55)
    company_address = models.CharField(max_length=55)
    
    def __str__(self):
        return self.company_name
    

    
    
    