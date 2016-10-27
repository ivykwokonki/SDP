from django.db import models

class Profile(models.Model):
    ABusername = models.CharField(max_length=8)
    password = models.CharField(max_length=15)


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

# Create your models here.
