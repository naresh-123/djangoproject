from django.db import models
class Productdata(models.Model):
    productnumber=models.IntegerField()
    productname=models.CharField(max_length=20)
    productcost=models.IntegerField()
    productclass=models.CharField(max_length=10)
    productweight=models.IntegerField()
