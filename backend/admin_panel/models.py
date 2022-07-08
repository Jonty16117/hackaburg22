from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)