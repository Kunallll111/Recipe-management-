from django.db import models
from django.contrib.auth.models import User
from django.db.models import F


# Create your models here.
class recipe(models.Model):
    user = models.ForeignKey(User , on_delete= models.SET_NULL ,null =True , blank=True)
    recipe_name =  models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to = "racipe")
    recipe_view_count = models.IntegerField(default=1)
    
