from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    fields = ('ABusername', 'currentCourse','latestModule','user')
