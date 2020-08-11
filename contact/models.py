from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Conatct(models.Model):

    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    contact_of = models.ForeignKey(User, on_delete=models.CASCADE)
    