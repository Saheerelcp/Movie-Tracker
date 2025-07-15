from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=30)

class movies(models.Model):
    userid = models.ForeignKey(user,on_delete=models.CASCADE)
    poster = models.URLField()
    title= models.CharField(max_length=60)
    year = models.IntegerField()
    status = models.CharField(max_length=20)