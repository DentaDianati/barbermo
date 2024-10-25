from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.IntegerField(unique=True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname']
    
    def __str__(self):
        return self.firstname + " " + self.lastname
