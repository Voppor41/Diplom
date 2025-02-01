from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=128)
    age = models.IntegerField()

class News(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
