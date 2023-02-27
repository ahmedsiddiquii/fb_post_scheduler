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
    post_as = models.CharField(max_length=200, default=None)
    every = models.CharField(max_length=200, default=None,choices=GENDER_CHOICES)
    time = models.TimeField(default=None)
    group = models.CharField(max_length=200, default=None)
    image = models.ImageField(upload_to="images/",default=None,blank=True)
    username = models.CharField(max_length=100, default=None,null=True)
    status = models.CharField(max_length=100, default=None, null=True)

    def update_choices(self, user):
        # Get data from ModelB for the current user and generate choices
        obj = list(PageModel.objects.filter(username=user).values())
        choices = [(user, user)]
        for i in obj:
            print(i)
            choices.append((i['page_id'], i['page_id']))
        choices = tuple(choices)

        self._meta.get_field('post_as').choices = choices
        return choices

