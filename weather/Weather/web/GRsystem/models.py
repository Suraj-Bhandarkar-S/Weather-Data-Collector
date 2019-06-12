from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.validators import RegexValidator



class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name
    
    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'


class graph(models.Model):
    city=models.CharField(max_length=25)
    Date=models.DateField()
    Temp=models.FloatField(max_length=6)

    def __str__(self):
        return self.city