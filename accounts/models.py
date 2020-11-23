from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    inquiry = models.CharField(max_length=400)
    phone = models.CharField(max_length=400, blank=True)

class Agents(models.Model):
    agency = models.CharField(max_length= 100)
    email = models.CharField(max_length= 100)
    contact = models.CharField(max_length= 100)
    phone = models.CharField(max_length= 100, blank = False)
    message = models.CharField(max_length= 100)
    resume = models.FileField()

class Quote(models.Model):
    contact_person= models.CharField(max_length= 100)
    company_name= models.CharField(max_length= 200)
    operations= models.CharField(max_length= 1000)
    phone = models.CharField(max_length= 1000)
    email = models.CharField(max_length= 100,blank=False, null= False)
    num_employee = models.IntegerField()
    payroll = models.FloatField()
