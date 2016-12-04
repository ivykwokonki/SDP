from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from SDP_API.models import Profile, User
from .forms import UserForm

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/Participant/availableCourse/")

    elif request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html',{'error': "Wrong Username or Password! Try again!"})
        elif user.is_active:

            auth.login(request,user)
            return HttpResponseRedirect("/Participant/availableCourse/")

        else:
            print("why not valid")
            return render(request, 'login.html',{'error': "Wrong Username or Password! Try again!"})
    else:
        print("why not post")
        return render(request, 'login.html')

def register(request):

    if request.POST:
        print(request.POST)
        form_class = UserForm
        form = form_class(request.POST)
        # ABusername = request.POST.get('ABusername', '')
        # ABusername_exist = Profile.objects.filter(ABusername=ABusername,)

        # if ABusername_exist.count()==0:
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            Profile.objects.create(
                user=user
            )

            g = Group.objects.get(name='Participant')
            g.user_set.add(user)

            # to do: need to save ABusername also
            # to do: need to default a partic role to user

            user = auth.authenticate(username=username, password=password)

            auth.login(request, user)
            return HttpResponseRedirect("/Participant/availableCourse/")

        #
        # else:
        #     return HttpResponse("This ABusername have already been registered")



    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')
