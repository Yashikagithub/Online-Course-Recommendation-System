from django.db import models
from django.contrib.auth.models import User




# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    topics = models.CharField(max_length=100)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField()


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video = models.URLField(max_length=200)

class Profile(models.Model):  # New Profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    field_of_interest = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username