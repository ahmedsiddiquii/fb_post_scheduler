from django.db import models

# Create your models here.
class Comments(models.Model):
    group_id = models.CharField(max_length=200 ),
    group_name = models.CharField(max_length=200 ),
    
class post(models.Model):
    post_id = models.CharField(max_length=200 ),
    post_title = models.CharField(max_length=200 ),
    post_time = models.CharField(max_length=200 ),
    status=models.CharField(max_length=200 ),
