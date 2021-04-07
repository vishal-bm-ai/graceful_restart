from django.db import models

# Create your models here.

class Count(models.Model):
    cnt = models.IntegerField()