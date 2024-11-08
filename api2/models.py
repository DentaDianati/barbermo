from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Barber(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    money = models.IntegerField(default=0)
    t1 = models.BooleanField(default=False)
    t2 = models.BooleanField(default=False)
    t3 = models.BooleanField(default=False)
    t4 = models.BooleanField(default=False)
    t5 = models.BooleanField(default=False)
    t6 = models.BooleanField(default=False)
    t7 = models.BooleanField(default=False)
    t8 = models.BooleanField(default=False)
    t9 = models.BooleanField(default=False)
    t10 = models.BooleanField(default=False)
    t11 = models.BooleanField(default=False)
    t12 = models.BooleanField(default=False)
    t13 = models.BooleanField(default=False)
    t14 = models.BooleanField(default=False)
    t15 = models.BooleanField(default=False)
    t16 = models.BooleanField(default=False)
    t17 = models.BooleanField(default=False)
    t18 = models.BooleanField(default=False)
    t19 = models.BooleanField(default=False)
    t20 = models.BooleanField(default=False)
    t21 = models.BooleanField(default=False)
    t22 = models.BooleanField(default=False)
    t23 = models.BooleanField(default=False)
    t24 = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name
