from django.shortcuts import render
from SDP_API.models import Course, Category, User, Instructor, Module, Component
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from SDP_API.forms import DocumentForm
from django.db.models import F

from django.core.urlresolvers import reverse

@login_required
def created_courses_view(request):
    currUserID = request.user.id
    currInstructor = Instructor.objects.get(user=currUserID)
    courses = Course.objects.filter(instructor=currInstructor)

    categorys = Category.objects.all()

    if 'courseID' in request.GET:
        course = Course.objects.get(id=request.GET['courseID'])
        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList})
    else:
        return render(request, 'createdCourses.html', {'courses': courses,'categorys':categorys})

@login_required
def created_module_view(request):
    currUserID = request.user.id
    currInstructor = Instructor.objects.get(user=currUserID)
    courses = Course.objects.filter(instructor=currInstructor)

    categorys = Category.objects.all()

    if 'courseID' in request.GET:
        course = Course.objects.get(id=request.GET['courseID'])
        module = Module.objects.get(id=request.GET['moduleID'])
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})
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

        # moduleList =
        noOfModule = Module.objects.filter(course_id=request.GET['courseID']).count()
        moduleOrder = request.POST['moduleOrder']
        Module.objects.filter(course_id=request.GET['courseID'], order__gte=moduleOrder).update(order=F('order')+1)
        UserID = request.user.id
        Module.objects.create(
            course_id = request.GET['courseID'],
            name = moduleName,
            order = moduleOrder,
        )

        course.no_of_module = course.no_of_module+1
        course.save()
        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList})
    else: #attempt to create module
        return render(request, 'createModule.html', {'course': course})

@login_required
def create_component(request):
    module = Module.objects.get(id=request.GET['moduleID'])
    course = Course.objects.get(id=request.GET['courseID'])
    form = DocumentForm(request.POST, request.FILES)
    if request.POST:
        print(request.POST)
        print(request.GET)
        componentName = request.POST['componentName']
        type = request.POST['componentType']
        UserID = request.user.id
        componentOrder = request.POST['componentOrder']
        Component.objects.filter(course_id=request.GET['courseID'], order__gte=componentOrder).update(order=F('order')+1)


        if (type == '0'):
            text_content = request.POST['text_content']

            Component.objects.create(
                course_id=request.GET['courseID'],
                module_id=request.GET['moduleID'],
                name=componentName,
                type=type,
                text_content=text_content,
                order = componentOrder,
            )
            print("text yes!")
        if (type == '1'):
            link = request.POST['link'];

            Component.objects.create(
                course_id=request.GET['courseID'],
                module_id=request.GET['moduleID'],
                name=componentName,
                type=type,
                link=link,
                order = componentOrder,
            )

        if (type == '2'):


            if form.is_valid():
                print ("file ok!")
                file =request.FILES['docfile']
                print(file)
                Component.objects.create(
                    course_id=request.GET['courseID'],
                    module_id=request.GET['moduleID'],
                    name=componentName,
                    type=type,
                    file=file,
                    order = componentOrder
                )
            else:
                print ("file Not Ok!")
                print(form)
                form = DocumentForm()
            # return render(request, 'createComponent.html', {'course': course, 'module': module})

        if (type == '3'):
            link = request.POST['link'];

            Component.objects.create(
                course_id=request.GET['courseID'],
                module_id=request.GET['moduleID'],
                name=componentName,
                type=type,
                link=link,
                order = componentOrder,
            )

        if (type == '4'):
            Component.objects.create(
                course_id=request.GET['courseID'],
                module_id=request.GET['moduleID'],
                name=componentName,
                type=type,
                order = componentOrder,
            )

        module.no_of_component = module.no_of_component+1
        module.save()
        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})
    else: #attempt to create component
        return render(request, 'createComponent.html', {'course': course, 'module': module,'form': form})
    #
    # module = Module.objects.get(id=request.GET['moduleID'])
    # course = Course.objects.get(id=request.GET['courseID'])
    # if request.POST:
    #     print(request.POST)
    #     print(request.FILES)
    #     componentName = request.POST['componentName']
    #     type = request.POST['componentType']
    #
    #     UserID = request.user.id  # by that instructor
    #
    #
    #     moduleList = Module.objects.filter(course_id=request.GET['courseID'])
    #     componentList = Component.objects.filter(course_id=request.GET['courseID'])
    #     return render(request, 'createdCourse.html',
    #                   {'course': course, 'moduleList': moduleList, 'componentList': componentList})
    # else:  # attempt to create component
    #     return render(request, 'createComponent.html', {'course': course, 'module': module})

@login_required
def component_move_up(request):
    try:
        course = Course.objects.get(id=request.GET['courseID'])
        module = Module.objects.get(id=request.GET['moduleID'])
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        currentComponent = Component.objects.get(id=request.GET['componentID'])
        currentOrder = currentComponent.order
        upperComponent = Component.objects.get(course_id=request.GET['courseID'], module_id=request.GET['moduleID'], order=currentOrder-1)
        upperComponent.order = currentOrder
        upperComponent.save()
        currentComponent.order = currentOrder-1
        currentComponent.save()
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})
    except:
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})

@login_required
def component_move_down(request):
    try:
        course = Course.objects.get(id=request.GET['courseID'])
        module = Module.objects.get(id=request.GET['moduleID'])
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        currentComponent = Component.objects.get(id=request.GET['componentID'])
        currentOrder = currentComponent.order
        lowerComponent = Component.objects.get(course_id=request.GET['courseID'], module_id=request.GET['moduleID'], order=currentOrder+1)
        lowerComponent.order = currentOrder
        lowerComponent.save()
        currentComponent.order = currentOrder+1
        currentComponent.save()
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})
    except:
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})

@login_required
def module_move_up(request):
    try:
        course = Course.objects.get(id=request.GET['courseID'])
        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        currentModule = Module.objects.get(id=request.GET['moduleID'])
        currentOrder = currentModule.order
        upperModule = Module.objects.get(course_id=request.GET['courseID'], order=currentOrder-1)
        upperModule.order = currentOrder
        upperModule.save()
        currentModule.order = currentOrder-1
        currentModule.save()
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList})
    except:
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList})

@login_required
def module_move_down(request):
    try:
        course = Course.objects.get(id=request.GET['courseID'])
        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        currentModule = Module.objects.get(id=request.GET['moduleID'])
        currentOrder = currentModule.order
        lowerModule = Module.objects.get(course_id=request.GET['courseID'], order=currentOrder+1)
        lowerModule.order = currentOrder
        lowerModule.save()
        currentModule.order = currentOrder+1
        currentModule.save()
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList})
    except:
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList})
