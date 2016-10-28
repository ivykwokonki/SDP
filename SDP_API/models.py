from django.db import models



class Profile(models.Model):
    class Meta:
        verbose_name = "AB User"

    class Role_choice:
        INSPECTOR = 0
        PARTICIPANTS = 1
        ADMIN = 2
        HR = 3

    ABuserID = models.CharField(max_length=8)
    username = models.ForeignKey(User, unique = True)
    is_instructor = models.BooleanField(default=False)
    is_HR = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    currentSession = models.PositiveSmallIntegerField(choices=Role_choice, default=1)
    currentCourse = models.ForeignKey(Course)
    lastestModule = models.ForeignKey(Module)

class Instructor(models.Model):
    username = models.ForeignKey(User, unique=True)
    permission_createCourse = models.BooleanField(default=False)
    permission_modifyCourse = models.BooleanField(default=False)

class CourseHistroy(models.Model):
    completed_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course)
    username = models.ForeignKey(User, unique=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_opened = models.BooleanField(default=False)
    category = models.ForeignKey(Category)
    instructor = models.ForeignKey(Instructor)
    orderOfModule = models.TextField(blank=True);

class Module(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course)

class Component(models.Model):
    class Type_choice:
        TEXT = 0
        PHOTO = 1
        FILE = 2
        QUIZ = 3

    type = models.PositiveSmallIntegerField(choices=Type_choice,)
    link = models.URLField(max_length=100)
    course = models.ForeignKey(Course)
    module = models.ForeignKey(Module)

