from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='Deleted User')[0]

# Create your models here.

class companyCompare(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    longdesc = models.TextField(blank=True)
    
    ppp = models.FloatField(null=True)
    plasticPpp = models.FloatField(null=True)
    testField1 = models.FloatField(max_length=200,default=-1)
    testField2 = models.FloatField(max_length=200,default=-1)
    testField3 = models.FloatField(max_length=200,default=-1)
    testField4 = models.FloatField(max_length=200,default=-1)
    testField5 = models.FloatField(max_length=200,default=-1)
    testField6 = models.FloatField(max_length=200,default=-1)
    testField7 = models.FloatField(max_length=200,default=-1)
    testField8 = models.FloatField(max_length=200,default=-1)
    testField9 = models.FloatField(max_length=200,default=-1)

    lat = models.FloatField(max_length=200,blank=True,null=True)
    long = models.FloatField(max_length=200,blank=True,null=True)

    tags = models.TextField(blank=True)
    def __str__(self):
        return self.name



class blogpost(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey("auth.user",on_delete=models.SET(get_sentinel_user))
    desc = models.TextField(blank=True)
    content = models.TextField()
    script = models.TextField(blank=True)

    compares = models.ManyToManyField(companyCompare,blank=True)
    def __str__(self):
        return self.name + " by " + self.author.first_name + " " + self.author.last_name

class attachment(models.Model):
    post = models.ForeignKey(blogpost, on_delete=models.CASCADE)
    file = models.FileField(upload_to="processAsset/")
    link = models.TextField(blank=True)
    def __str__(self):
        return self.file.filename

class mcpsSchool(models.Model):
    schooltype_choices = [("elementarty","Elementary School"),("middle","Middle School"),("high","High School"),("special","Special Schools")]
    schooltype = models.CharField(max_length=20,choices=schooltype_choices,default="high")
    name = models.CharField(max_length=500)
    ppp_2014_2015 = models.FloatField(max_length=200)
    ppp_2015_2016 = models.FloatField(max_length=200)
    ppp_2016_2017 = models.FloatField(max_length=200)
    ppp_2017_2018 = models.FloatField(max_length=200)
    ppp_2018_2019 = models.FloatField(max_length=200)
    ppp_2014_2015_rank = models.FloatField(max_length=200)
    ppp_2015_2016_rank = models.FloatField(max_length=200)
    ppp_2016_2017_rank = models.FloatField(max_length=200)
    ppp_2017_2018_rank = models.FloatField(max_length=200)
    ppp_2018_2019_rank = models.FloatField(max_length=200)
    lat = models.FloatField(max_length=200)
    long = models.FloatField(max_length=200)
    desc = models.TextField(blank=True,null=True)
    link = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.schooltype + " - " + self.name

class pums(models.Model):
    code = models.CharField(max_length=500)
    geodata = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.code

class zipcode(models.Model):
    code = models.CharField(max_length=10)
    geodata = models.TextField(blank=True,null=True)
    area = models.FloatField()
    population = models.BigIntegerField()
    average_income = models.FloatField(max_length=200)
    density = models.FloatField()
    def __str__(self):
        return self.code

