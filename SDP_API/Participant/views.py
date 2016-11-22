from django.shortcuts import render
from django.http import HttpResponseRedirect
from SDP_API.models import Course, User, Profile, Category, Module, Component
from django.contrib.auth.decorators import login_required

@login_required
def AvailableCourseView(request):
    courses = Course.objects.filter(is_opened=True)
    categorys = Category.objects.all()


    if 'category' in request.GET and request.GET['category'] != 'all':
        courses = courses.filter(category=request.GET['category'])
        return render(request, 'availableCourse.html', {'courses': courses,'categorys':categorys})
    else:
        return render(request, 'availableCourse.html', {'courses':courses,'categorys':categorys})


@login_required
def currentCourseView(request):
    currUserID = request.user.id
    currCourseID = Profile.objects.get(user=currUserID).currentCourse
    course = Course.objects.get(id=currCourseID)

    moduleList = Module.objects.filter(course_id=currCourseID)
    componentList = Component.objects.filter(course_id=currCourseID)
    return render(request, 'currentCourses.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList} )

@login_required
def enrollment(request):

    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.filter(user=request.user.id)[0]

    if 'enroll' in request.GET:

        if profile.currentCourse == -999:
            courseid = int(request.GET['enroll'])
            course = Course.objects.get(id=courseid)
            profile.currentCourse = courseid
            profile.save()
        else:
            course = Course.objects.get(id=profile.currentCourse)
            return render (request, 'enrollment.html', {'profile': profile, 'course': course, 'error': "Only one course at a time."})
    else:
        if profile.currentCourse == -999:
            return render(request, 'enrollment.html', {'profile': profile})

    course = Course.objects.get(id=profile.currentCourse)
    return render(request, 'enrollment.html', {'profile': profile, 'course': course})





