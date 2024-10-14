from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(null=False,max_length=20)
    lastname= models.CharField(null=False,max_length=30)
    password= models.CharField(null=False,max_length=20)




