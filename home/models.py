from django.db import models

# Create your models here.
class student(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length= 254)
    address = models.TextField(max_length= 200)
    
class product(models.Model):
    pass

class car(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
    
    