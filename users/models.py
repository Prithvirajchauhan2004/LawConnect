from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ServiceProvider(models.Model):
    '''personal details'''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100, null=True)
    last_name = models.CharField(max_length = 100, null=True)
    DOB = models.CharField(max_length = 30, null=True)
    Gender = models.CharField(max_length = 20, null=True)
    work_as = models.CharField(max_length =100, null=True)
    father_first_name = models.CharField(max_length = 100, null=True)
    father_last_name = models.CharField(max_length = 100, null=True)
    interest = models.CharField(max_length = 100, null=True)
    '''contact'''
    ph_number = models.BigIntegerField()#this
    alt_number = models.BigIntegerField(null=True)
    email = models.EmailField()#this
    '''ADDRESS'''
    add = models.CharField(max_length = 100, null=True)
    city = models.CharField(max_length = 100, null=True)
    state = models.CharField(max_length = 100, null=True)
    pin_code = models.IntegerField( null=True)
    country = models.CharField(max_length = 150, null=True)
    '''educational details'''
    college = models.CharField(max_length = 200, null=True)
    course_desc = models.TextField(null=True)
    '''work details'''
    company = models.CharField(max_length = 150, null=True)
    work_desc = models.TextField(null=True)
    '''documnets'''
    adhar = models.ImageField(null=True)
    bar_certificate = models.ImageField(null=True)




class Client(models.Model):

    username = models.CharField(max_length = 100)
    email = models.EmailField()
    tel = models.BigIntegerField()
    password = models.CharField(max_length = 50)