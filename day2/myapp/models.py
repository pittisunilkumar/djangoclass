from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(null=False,max_length=100)
    section= models.CharField(null=True,max_length=10)
    password=models.CharField(null=False,max_length=100)
    lastname=models.CharField(null=False,max_length=100,default='')

    def __str__(self):
        return self.name

