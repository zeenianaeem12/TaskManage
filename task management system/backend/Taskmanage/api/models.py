from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=15)
