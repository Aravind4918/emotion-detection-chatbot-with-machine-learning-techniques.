from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    ph = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    gen = models.CharField(max_length=100)
    age = models.IntegerField()
    addr = models.TextField()
    statu=models.IntegerField()

    

class accval(models.Model):
    alg_name = models.CharField(max_length=100)
    sc1 = models.FloatField()
    sc2 = models.FloatField()
    sc3 = models.FloatField()
    sc4 = models.FloatField()

    



class queries(models.Model):
    q_n=models.CharField(max_length=1000);
    an_s=models.CharField(max_length=1000);

class chat(models.Model):
    name=models.CharField(max_length=100);
    email=models.CharField(max_length=100);
    message=models.CharField(max_length=100);

class content(models.Model):
    category=models.CharField(max_length=100);
    d_type=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    data=models.CharField(max_length=100);

class tdetails(models.Model):
    name=models.CharField(max_length=100);
    qualification=models.CharField(max_length=100);
    address=models.CharField(max_length=1000);
    city=models.CharField(max_length=100);
    

