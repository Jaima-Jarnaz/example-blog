from django.db import models
class Customer(models.Model):
    firstname =models.CharField(max_length=100)
    lastname  =models.CharField(max_length=100)
    email     =models.EmailField()
    password  =models.CharField(max_length=100)
    confirmpassword  =models.CharField(max_length=100)
