from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)



class Teacher(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    professional =models.CharField(max_length=30, blank=False, default='')
    age = models.CharField(max_length=3,blank=True, default='' )
    onDuty = models.BooleanField(default= False)