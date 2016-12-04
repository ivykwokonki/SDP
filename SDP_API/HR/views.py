from django.shortcuts import render
from SDP_API.models import User, CourseHistroy, Course, Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def search(request):

    if 'tarUserID' in request.GET:
        tarUserID = int(request.GET['tarUserID'])
        tarUser = User.objects.get(id=tarUserID)

        historyList = CourseHistroy.objects.filter(user_id=tarUserID)

        if historyList.count()>0:
            tarProfile = Profile.objects.get(user_id=tarUserID)
            courseList = Course.objects.all()
            return render(request, 'viewStaff.html', {'tarUser': tarUser, 'tarProfile': tarProfile, 'historyList': historyList, 'courseList': courseList})
        else:
            return render(request, 'viewStaff.html', {'tarUser': tarUser})


    users = User.objects.all()
    return render(request, 'viewStaff.html', {'users': users})
