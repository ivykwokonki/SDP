from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    class Meta:
        verbose_name = "AB User"

    class Role_choice:
<<<<<<< HEAD
        INSTRUCTOR = 0
=======
        INSPECTOR = 0
>>>>>>> 8e243536a82e712500a8e12486fd0ceb98571605
        PARTICIPANTS = 1
        ADMIN = 2
        HR = 3

    ABuserID = models.CharField(max_length=8)
    username = models.ForeignKey(User, unique = True)
<<<<<<< HEAD
    role = models.PositiveSmallIntegerField(choices=Role_choice, )
    #CourseList

class CourseHistroy(models.Model):
    completed_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course)
    username = models.ForeignKey(User, unique=True)

=======
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

>>>>>>> 8e243536a82e712500a8e12486fd0ceb98571605
class Category(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_opened = models.BooleanField(default=False)
    category = models.ForeignKey(Category)
<<<<<<< HEAD
    # ModuleList
=======
    instructor = models.ForeignKey(Instructor)
    orderOfModule = models.TextField(blank=True);
>>>>>>> 8e243536a82e712500a8e12486fd0ceb98571605

class Module(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course)
<<<<<<< HEAD
    # ComponentList
=======
>>>>>>> 8e243536a82e712500a8e12486fd0ceb98571605

class Component(models.Model):
    class Type_choice:
        TEXT = 0
        PHOTO = 1
        FILE = 2
        QUIZ = 3

    type = models.PositiveSmallIntegerField(choices=Type_choice,)
    link = models.URLField(max_length=100)
<<<<<<< HEAD
=======
    course = models.ForeignKey(Course)
>>>>>>> 8e243536a82e712500a8e12486fd0ceb98571605
    module = models.ForeignKey(Module)

