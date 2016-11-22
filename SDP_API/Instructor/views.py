from django.shortcuts import render
from SDP_API.models import Course, Category, User, Instructor, Module, Component
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def created_courses_view(request):
    currUserID = request.user.id
    currInstructor = Instructor.objects.get(user=currUserID)
    courses = Course.objects.filter(instructor=currInstructor)

    categorys = Category.objects.all()

    if 'courseID' in request.GET:
        course = Course.objects.get(id=request.GET['courseID'])
        moduleList = Module.objects.filter(course_id=request.GET['courseID'])
        componentList = Component.objects.filter(course_id=request.GET['courseID'])
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList})
    else:
        return render(request, 'createdCourses.html', {'courses': courses,'categorys':categorys})

@login_required
def release_course(request):
    if request.method == 'POST' and 'releaseCourseID' in request.POST:
        releaseCourseID = request.POST.get("releaseCourseID") #['releaseCourseID']
        if releaseCourseID is None:
            return HttpResponse(status=400)
        releaseCourse = Course.objects.get(id=releaseCourseID)
        releaseCourse.is_opened = True
        releaseCourse.save()

        return HttpResponse("success")
    else:
        return HttpResponse(status=400)

@login_required
def create_course(request):
    if request.POST:

        CourseName = request.POST['CourseName']
        CourseDescription = request.POST['CourseDesc']

        CourseCategoryID = request.POST['CourseCategory']
        CourseCategory = Category.objects.get(id=CourseCategoryID)

        #to do
        UserID = 2
        CourseInstructor = Instructor.objects.get(user=UserID)
        Course.objects.create(
            name = CourseName,
            description = CourseDescription,
            category = CourseCategory,
            instructor = CourseInstructor
        )
        return HttpResponseRedirect ("/Instructor/createdCourses/")
    else:
        categorys = Category.objects.all()
        return render(request, 'createCourse.html', {'categorys':categorys} )

@login_required
def create_module(request):
    course = Course.objects.get(id=request.GET['courseID'])
    if request.POST:
        moduleName = request.POST['moduleName']

        UserID = request.user.id
        Module.objects.create(
            course_id = request.GET['courseID'],
            name = moduleName,
        )
        moduleList = Module.objects.filter(course_id=request.GET['courseID'])
        componentList = Component.objects.filter(course_id=request.GET['courseID'])
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList})
    else: #attempt to create module
        return render(request, 'createModule.html', {'course': course})

@login_required
def create_component(request):
    module = Module.objects.get(id=request.GET['moduleID'])
    course = Course.objects.get(id=request.GET['courseID'])
    if request.POST:
        print(request.POST)
        print(request.GET)
        componentName = request.POST['componentName']
        type = request.POST['componentType']
        UserID = request.user.id
        Component.objects.create(
            course_id = request.GET['courseID'],
            module_id = request.GET['moduleID'],
            name = componentName,
            type = type,
        )

        moduleList = Module.objects.filter(course_id=request.GET['courseID'])
        componentList = Component.objects.filter(course_id=request.GET['courseID'])
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList})
    else: #attempt to create component
        return render(request, 'createComponent.html', {'course': course, 'module': module})
