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
from SDP_API import views as views
from SDP_API.Instructor import views as Instructor_views
from SDP_API.HR import views as HR_views
from SDP_API.Participant import views as Participant_views
from SDP_API.Admin import views as Admin_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', views.login),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/register/$', views.register),
    url(r'^Participant/availableCourse/$', Participant_views.AvailableCourseView),
    url(r'^Participant/currentCourse/$', Participant_views.currentCourseView),
    url(r'^Participant/enrollment/$', Participant_views.enrollment),
    url(r'^Participant/drop/$', Participant_views.drop),

    url(r'^Instructor/createCourse/$', Instructor_views.create_course),
    url(r'^Instructor/createdCourses/$', Instructor_views.created_courses_view),
    url(r'^Instructor/releaseCourse/$', Instructor_views.release_course),

    url(r'^Instructor/createdCourses/createModule/$', Instructor_views.create_module),
    url(r'^Instructor/createdCourses/createdModule/$', Instructor_views.created_module_view),
    url(r'^Instructor/createdCourses/createComponent/$', Instructor_views.create_component),

    url(r'^Instructor/createdCourses/componentMoveUp/$', Instructor_views.component_move_up),
    url(r'^Instructor/createdCourses/componentMoveDown/$', Instructor_views.component_move_down),
    url(r'^Instructor/createdCourses/moduleMoveUp/$', Instructor_views.module_move_up),
    url(r'^Instructor/createdCourses/moduleMoveDown/$', Instructor_views.module_move_down),
    url(r'^Instructor/createdCourses/deleteComponent/$', Instructor_views.delete_component),
    url(r'^Instructor/createdCourses/deleteModule/$', Instructor_views.delete_module),

    url(r'^Admin/userPermission/$', Admin_views.UserPermissionView),
    url(r'^Admin/editUserPermission/$', Admin_views.editUserPermission),
    url(r'^Admin/manageCategory/$', Admin_views.manageCategoryView),
    url(r'^Admin/editCategory/$', Admin_views.editCategory)


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
