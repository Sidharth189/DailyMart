from django.db import models
from adminpanel.models import categorydb,productdb

# Create your models here.

class contactdb(models.Model):
    cname=models.CharField(max_length=50)
    cemail=models.CharField(max_length=100)
    cmsg=models.CharField(max_length=500)

class userdb(models.Model):
    uname=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phno=models.IntegerField()
    password=models.CharField(max_length=50)

class cartdb(models.Model):
    user=models.ForeignKey(userdb,on_delete=models.SET_DEFAULT,default='')
    product=models.ForeignKey(productdb,on_delete=models.SET_DEFAULT,default='')
    total=models.IntegerField(default=0)
    status=models.IntegerField(default=0)
    quantity=models.IntegerField(default=1)

class shippingaddressdb(models.Model):
    user=models.ForeignKey(userdb,on_delete=models.SET_DEFAULT,default='')
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    street=models.CharField(max_length=100)
    building=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    notes=models.CharField(max_length=250)

