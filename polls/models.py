from django.db import models
from django.db import models
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# Create your models here.
class PageModel(models.Model):
    page_id = models.CharField(max_length=100, default=None)
    username = models.CharField(max_length=100,default=None)

class FBAccount(models.Model):
    email = models.CharField(max_length=100, default=None)
    password = models.CharField(max_length=100, default=None)
    username = models.CharField(max_length=100,default=None)
    status = models.CharField(max_length=100,default=None)
class PostModel(models.Model):
    GENDER_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    title = models.CharField(max_length=200, default=None)
    text = models.CharField(max_length=200, default=None)
    post_as = models.CharField(max_length=200, default=None,choices=None)
    every = models.CharField(max_length=200, default=None,choices=GENDER_CHOICES)
    time = models.TimeField(default=None)
    group = models.CharField(max_length=200, default=None)
    image = models.ImageField(upload_to="images/",default=None,blank=True)
    username = models.CharField(max_length=100, default=None,null=True)
    status = models.CharField(max_length=100, default=None, null=True)
