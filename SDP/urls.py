"""SDP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from SDP_API.Instructor import views as Instructor_views
from SDP_API.HR import views as HR_views
from SDP_API.Participant import views as Participant_views
from SDP_API.Admin import views as Admin_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Instructor/createCourse/$', Instructor_views.create_course,name='create_course'),
]
