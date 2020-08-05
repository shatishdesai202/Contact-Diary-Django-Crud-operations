from django.db import models

# Create your models here.

class Conatct(models.Model):

    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    