from django.db import models

# Create your models here.
class Spider(models.Model):
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)