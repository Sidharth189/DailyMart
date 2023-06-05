from django.db import models

# Create your models here.

class categorydb(models.Model):
    name=models.CharField(max_length=50)
    descr=models.CharField(max_length=250)

class productdb(models.Model):
    pname=models.CharField(max_length=50)
    pdescr=models.CharField(max_length=500)
    price=models.IntegerField()
    pimg=models.ImageField(upload_to='productimg',default='null.jpg')
    pcategory=models.CharField(max_length=50,default='')
