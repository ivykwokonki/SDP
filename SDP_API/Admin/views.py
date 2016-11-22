from django.shortcuts import render
from SDP_API.models import Course, Category, User, Instructor, Profile
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import Group

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


def editUserPermission(request):
    if request.POST:

        group = request.POST['group']
        userID = request.POST['user_id']
        request_type = request.POST['request_type'] #True: add to group / False: remove from group

        g = Group.objects.get(name=group)
        user = User.objects.get(id=userID)

        if  request_type==True:
            g.user_set.add(user)
        else:
            g.user_set.remove(user)

        return HttpResponse("success")

    else:
        return HttpResponse(status=400)


def manageCategoryView(request):
    if request.POST['newCategory']:
        newCategoryName = request.POST['newCategory']
        if(Category.objects.get(name=newCategoryName)):
            return HttpResponse("duplicate category name ! ")
        else:
            Category.objects.create(
                name = newCategoryName,
            )

    elif request.POST['renameCategoryID']:  #rename
        renameCategory = Category.objects.get(id=request.POST['renameCategoryID'])
        renameCategory.name = request.POST['renameCategory']
        renameCategory.save()

    elif request.POST['deleteCategoryID']:    #delete
        renameCategory = Category.objects.get(id=request.POST['deleteCategoryID'])
        renameCategory.name = request.POST['renameCategory']
        renameCategory.delete()

    category = Category.objects.all()
    return render(request, 'editCategory.html', {'category': category})
