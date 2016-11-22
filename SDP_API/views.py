from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/Participant/availableCourse/")

    elif request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = auth.authenticate(username=username,password =password)

        if user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect("/Participant/availableCourse/")
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')
