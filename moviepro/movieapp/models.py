from django.db import models
class Telugu(models.Model):
    director_name=models.CharField(max_length=20)
    hero_name=models.CharField(max_length=20)
    heroin_name=models.CharField(max_length=20)
    product_name=models.CharField(max_length=20)
    released_date=models.DateTimeField()
    def __str__(self):
        return self.director_name
class English(models.Model):
    director_name=models.CharField(max_length=20)
    hero_name=models.CharField(max_length=20)
    heroin_name=models.CharField(max_length=20)
    product_name=models.CharField(max_length=20)
    released_date=models.DateTimeField()
    def __str__(self):
        return self.director_name
class Hindhi(models.Model):
    director_name=models.CharField(max_length=20)
    hero_name=models.CharField(max_length=20)
    heroin_name=models.CharField(max_length=20)
    product_name=models.CharField(max_length=20)
    released_date=models.DateTimeField()
    def __str__(self):
        return self.director_name

class Userdata(models.Model):
    moviename1=models.CharField(max_length=20)
    username1=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    mobile1=models.BigIntegerField(max_length=10)
    adharnumber1=models.CharField(max_length=13)
    showtime1=models.DateTimeField()