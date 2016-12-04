from django.shortcuts import render
from SDP_API.models import Course, Category, User, Instructor, Profile
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

@login_required
def UserPermissionView(request):
    if 'username' in request.GET:
        #search this username
        print("hihi")
    else:
        profile = Profile.objects.all()
        user = User.objects.all()
        group = Group.objects.all()
        instructor = Instructor.objects.all()
        return render(request, 'userPermission.html', {'user': user,'profile': profile, 'group': group, 'instructor': instructor})

@login_required
def editUserPermission(request):
    # if request.method == 'POST' and 'userID' in request.POST:
    if request.method == 'POST':

        userID = request.POST['userID']
        user = User.objects.get(id=userID)
        is_allowed = request.POST['is_allowed']  # True: add to group / False: remove from group
        request_type = request.POST['request_type']
        # 1:permission of hr, admin, instructor
        # 2:permision of instructor: i)create ii)manage course
        # 3:permission of access SDP : set user.acitve = False


        if(request_type=="1"):
            print("enter 1")
            print(is_allowed)
            group = request.POST['permission_name']
            # if(group!="Instructor") or (group!="HR_staff") or (group!="Administrator"):
            #     return HttpResponse(status=400)
            if(group=="Instructor"):
                if(is_allowed=="true"):
                    Instructor.objects.create(
                        user=user
                    )
                else:
                    instructor = Instructor.objects.get(user=user)
                    instructor.delete()
                    instructor.save()

            g = Group.objects.get(name=group)

            if (is_allowed=="true"):

                g.user_set.add(user)
            else:
                print("gg")
                g.user_set.remove(user)

            return HttpResponse("success")


        elif(request_type=='2'):

            instructor = Instructor.objects.get(user=user)
            permission = request.POST['permission_name']
            if(permission=="create"):
                print("enter create")
                if (is_allowed == "true"):
                    instructor.permission_createCourse = True
                else:
                    instructor.permission_createCourse = False
                instructor.save()
                return HttpResponse("success")
            elif(permission=="modify"):
                print("enter modify")
                if (is_allowed == "true"):
                    instructor.permission_modifyCourse = True
                else:
                    instructor.permission_modifyCourse = False
                instructor.save()
                return HttpResponse("success")
            else:
                print("gg")
                return HttpResponse(status=400)


        elif(request_type=='3'):
            print("enter 3")
            if(is_allowed =="true"):
                user.is_active = True
                user.save()
            else:
                user.is_active = False
                user.save()
            return HttpResponse("success")

    else:
        return HttpResponse(status=400)


@login_required
def manageCategoryView(request):

    category = Category.objects.all()
    return render(request, 'manageCategory.html', {'category': category})

@login_required
def editCategory(request):
    if request.POST:
        print(request.POST)
        deleteCategory_request = request.POST.get("deleteCategory", "-")
        renameCategory_request = request.POST.get("renameCategory", "-")
        newCategoryName_request = request.POST.get("newCategoryName", "-")
        # print("rename")
        if deleteCategory_request is not "-":    #delete
            deleteCategory = Category.objects.get(id=request.POST['deleteCategory'])
            print(deleteCategory)
            deleteCategory.delete()
            return HttpResponse("success")


        elif renameCategory_request is not "-":  #rename
            print("rename")
            renameCategory = Category.objects.get(id=request.POST['renameCategoryID'])
            renameCategory.name = request.POST['renameCategory']
            renameCategory.save()
            return HttpResponse("success")


        elif newCategoryName_request is not "-":     #new category
            print("create")
            newCategoryName = request.POST['newCategoryName']
            Category_exist = Category.objects.filter(name=newCategoryName)
            if(Category_exist.count()>0):
                return HttpResponse("duplicate category name ! ")
            else:
                Category.objects.create(
                    name = newCategoryName,
                )
            return HttpResponse("success")


        # else:
        #     return HttpResponse("success")
    else:
        return HttpResponse(status=400)
