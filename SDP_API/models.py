from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    user = models.ForeignKey(User, primary_key=True, default=1)
    permission_createCourse = models.BooleanField(default=False)
    permission_modifyCourse = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_opened = models.BooleanField(default=False)
    category = models.ForeignKey(Category)
    instructor = models.ForeignKey(Instructor)
    orderOfModule = models.TextField(blank=True);

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.name


class Component(models.Model):
    class TYPE:
        TEXT = 0
        PHOTO = 1
        FILE = 2
        QUIZ = 3

    type_choices = (
        (TYPE.TEXT, "text"),
        (TYPE.PHOTO, "photo"),
        (TYPE.FILE, "file"),
        (TYPE.QUIZ, "quiz"),
    )
    name = models.CharField(max_length=100, default='component')
    type = models.PositiveSmallIntegerField(choices=type_choices, )
    link = models.URLField(max_length=100)
    course = models.ForeignKey(Course)
    module = models.ForeignKey(Module)

    def __str__(self):
        return self.id


class CourseHistroy(models.Model):
    completed_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user


class Profile(models.Model):
    class Meta:
        verbose_name = "AB User"

    user = models.ForeignKey(User, primary_key=True)
    ABusername = models.CharField(max_length=8, default='ABstaff0')
    currentCourse = models.IntegerField(default=-999)
    latestModule = models.IntegerField(default=-999)

    def __str__(self):
        return self.user
