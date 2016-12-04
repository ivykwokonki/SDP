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

        can_modify = modify_permission(currUserID)
        not_released = not_released_course(request.GET['courseID'])

        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList, 'componentList': componentList, 'not_released':not_released, 'can_modify':can_modify})
    else:
        can_create = create_permission(currUserID)
        print(can_create)
        return render(request, 'createdCourses.html', {'courses': courses,'categorys':categorys,'can_create':can_create})

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
        can_modify = modify_permission(currUserID)
        not_released = not_released_course(request.GET['courseID'])
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList, 'not_released':not_released, 'can_modify':can_modify})
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

        UserID = request.user.id
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
        moduleOrder = request.POST['moduleOrder']
        Module.objects.filter(course_id=request.GET['courseID'], order__gte=moduleOrder).update(order=F('order')+1)
        UserID = request.user.id
        course.no_of_module = course.no_of_module+1
        course.save()
        if (moduleOrder > course.no_of_component):
            moduleOrder = course.no_of_component

        Module.objects.create(
            course_id = request.GET['courseID'],
            name = moduleName,
            order = moduleOrder,
        )


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
        module.no_of_component = module.no_of_component+1
        module.save()
        if (componentOrder > module.no_of_component):
            componentOrder = module.no_of_component

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


        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})
    else: #attempt to create component
        return render(request, 'createComponent.html', {'course': course, 'module': module})

@login_required
def delete_component(request):
    try:
        course = Course.objects.get(id=request.GET['courseID'])
        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        module = Module.objects.get(id=request.GET['moduleID'])
        component = Component.objects.get(id=request.GET['componentID'])
        componentOrder = component.order
        component.delete()
        Component.objects.filter(course_id=request.GET['courseID'], order__gte=componentOrder).update(order=F('order')-1)
        module.no_of_component = module.no_of_component-1
        module.save()
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})
    except:
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})

@login_required
def edit_component(request):
    course = Course.objects.get(id=request.GET['courseID'])
    module = Module.objects.get(id=request.GET['moduleID'])
    component = Component.objects.get(id=request.GET['componentID'])
    form = DocumentForm(request.POST, request.FILES)
    if request.POST:
        print(request.POST)
        print(request.GET)
        componentName = request.POST['componentName']
        type = request.POST['componentType']
        UserID = request.user.id

        componentOrder = int(request.POST['componentOrder'])
        Component.objects.filter(course_id=request.GET['courseID'], order__gt=component.order, order__lte=componentOrder).update(order=F('order')-1)
        if (componentOrder > module.no_of_component):
            componentOrder = module.no_of_component

        if (type == '0'):
            text_content = request.POST['text_content']

            Component.objects.filter(id=component.id).update(
                name=componentName,
                type=type,
                text_content=text_content,
                order = componentOrder,
            )
            print("text yes!")
        if (type == '1'):
            link = request.POST['link'];

            Component.objects.filter(id=component.id).update(
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
                Component.objects.filter(id=component.id).update(
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

            Component.objects.filter(id=component.id).update(
                name=componentName,
                type=type,
                link=link,
                order = componentOrder,
            )

        if (type == '4'):
            Component.objects.filter(id=component.id).update(
                name=componentName,
                type=type,
                order = componentOrder,
            )


        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        return render(request, 'createdModule.html', {'course': course, 'module': module, 'componentList': componentList})
    else: #attempt to edit component
        return render(request, 'editComponent.html', {'course': course, 'module': module, 'component': component})

@login_required
def delete_module(request):
    try:
        course = Course.objects.get(id=request.GET['courseID'])
        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        module = Module.objects.get(id=request.GET['moduleID'])
        moduleOrder = module.order
        module.delete()
        Module.objects.filter(course_id=request.GET['courseID'], order__gte=moduleOrder).update(order=F('order')-1)
        course.no_of_module = course.no_of_module-1
        course.save()
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList})
    except:
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList})

@login_required
def edit_module(request):
    course = Course.objects.get(id=request.GET['courseID'])
    module = Module.objects.get(id=request.GET['moduleID'])
    if request.POST:
        moduleName = request.POST['moduleName']
        moduleOrder = int(request.POST['moduleOrder'])
        Module.objects.filter(course_id=request.GET['courseID'], order__gt=module.order, order__lte=moduleOrder).update(order=F('order')+1)
        UserID = request.user.id
        if (moduleOrder > course.no_of_module):
            moduleOrder = course.no_of_module

        Module.objects.filter(id=module.id).update(
            name = moduleName,
            order = moduleOrder,
        )


        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        componentList = Component.objects.filter(course_id=request.GET['courseID']).order_by('order')
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList})
    else: #attempt to edit module
        return render(request, 'editModule.html', {'course': course, 'module': module})

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
        currentModule = Module.objects.get(id=request.GET['moduleID'])
        currentOrder = currentModule.order
        upperModule = Module.objects.get(course_id=request.GET['courseID'], order=currentOrder-1)
        upperModule.order = currentOrder
        upperModule.save()
        currentModule.order = currentOrder-1
        currentModule.save()
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList})
    except:
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList})

@login_required
def module_move_down(request):
    try:
        course = Course.objects.get(id=request.GET['courseID'])
        moduleList = Module.objects.filter(course_id=request.GET['courseID']).order_by('order')
        currentModule = Module.objects.get(id=request.GET['moduleID'])
        currentOrder = currentModule.order
        lowerModule = Module.objects.get(course_id=request.GET['courseID'], order=currentOrder+1)
        lowerModule.order = currentOrder
        lowerModule.save()
        currentModule.order = currentOrder+1
        currentModule.save()
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList})
    except:
        return render(request, 'createdCourse.html', {'course': course, 'moduleList': moduleList})

#functions for reuse
def create_permission(Iid):

    instructor = Instructor.objects.filter(user_id=Iid)[0]
    if (instructor.permission_createCourse == True):
        return True
    else:
        return False

def modify_permission(Iid):

    instructor = Instructor.objects.filter(user_id=Iid)[0]
    if (instructor.permission_modifyCourse == True):
        return True
    else:
        return False

def not_released_course(courseID):
    course = Course.objects.filter(id=courseID)[0]
    if (course.is_opened == True):
        return False
    else:
        return True
