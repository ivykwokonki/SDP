from django.shortcuts import render
from django.http import HttpResponseRedirect
from SDP_API.models import Course, User, Profile, Category, Module, Component, CourseHistroy
from django.contrib.auth.decorators import login_required
from datetime import date

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
    profile = Profile.objects.get(user=currUserID)
    currCourseID = profile.currentCourse

    if currCourseID == -999:
        return render(request, 'currentCourses.html', {'error': "No current Course."})
    else:
        course = Course.objects.get(id=currCourseID)

        moduleList = Module.objects.filter(course_id=currCourseID).order_by('order')
        componentList = Component.objects.filter(course_id=currCourseID)
        return render(request, 'currentCourses.html',
                      {'profile': profile, 'course': course, 'moduleList': moduleList, 'componentList': componentList})


@login_required
def viewHistory(request):
    userID = request.user.id
    historyList = CourseHistroy.objects.filter(user_id=userID)
    courseList = Course.objects.all()
    return render(request, 'viewCourseHistory.html', {'historyList': historyList, 'courseList':courseList})

@login_required
def viewCourse(request):
    cid = int(request.GET['courseID'])
    course = Course.objects.get(id=cid)
    moduleList = Module.objects.filter(course_id=cid).order_by('order')
    return render(request, 'viewCourse.html', {'completed': 1, 'course': course, 'moduleList': moduleList})


@login_required
def viewComponent(request):

    currUserID = request.user.id
    profile = Profile.objects.get(user=currUserID)
    moduleID = int(request.GET['moduleID'])

    module = Module.objects.get(id=moduleID)

    if (profile.latestModule == module.order):
        profile.latestModule = module.order + 1;
        profile.save()

        courseID = int(request.GET['courseID'])
        completeCourse = Course.objects.get(id=courseID)
        if ((profile.latestModule != 9999) and (completeCourse.no_of_module < profile.latestModule)):

            record = CourseHistroy.objects.filter(course=completeCourse)
            print(record)

            if record.count() > 0:
                record[0].completed_at = date.today()
                record[0].save()
            else:
                currUser = User.objects.get(id=request.user.id)

                CourseHistroy.objects.create(
                    completed_at=date.today(),
                    course=completeCourse,
                    user=currUser
                )

            profile.latestModule = 9999;
            profile.save()

    componentList = Component.objects.filter(module_id=moduleID).order_by('order')
    if 'completed' in request.GET:
        return render(request, 'viewComponent.html', {'completed': 1, 'module': module, 'componentList': componentList})
    else:
        return render(request, 'viewComponent.html', {'module': module, 'componentList': componentList})



@login_required
def enrollment(request):

    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.filter(user=request.user.id)[0]

    if 'enroll' in request.GET:

        if ((profile.currentCourse == -999) or (profile.latestModule == 9999)):
            courseid = int(request.GET['enroll'])
            course = Course.objects.get(id=courseid)
            profile.currentCourse = courseid
            profile.latestModule = 1
            profile.save()
        else:
            course = Course.objects.get(id=profile.currentCourse)
            return render (request, 'enrollment.html', {'profile': profile, 'course': course, 'error': "Only one course at a time."})
    else:
        if profile.currentCourse == -999:
            return render(request, 'enrollment.html', {'profile': profile})

    course = Course.objects.get(id=profile.currentCourse)
    return render(request, 'enrollment.html', {'profile': profile, 'course': course})

@login_required
def drop(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.filter(user=request.user.id)[0]

    profile.currentCourse = -999
    profile.latestModule = -999
    profile.save()

    return render(request, 'enrollment.html', {'profile': profile})



