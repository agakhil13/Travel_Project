from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Banner(models.Model):
    faded_text = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    bold_text = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Banner')

class Box_Category(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Boxes')

class Hot_Tour(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    review = models.IntegerField()
    img = models.ImageField(upload_to='Hot_Tour')
    price = models.IntegerField()

class Teams(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=30)
    img = models.ImageField(upload_to='Team')

class Wonder(models.Model):
    img = models.ImageField(upload_to='Wonder')