from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.CharField(max_length=250)
