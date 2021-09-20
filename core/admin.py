from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import *

# admin.site.register(Students)
admin.site.register(Subject)
admin.site.register(Day)
admin.site.register(Homework)
admin.site.register(Class_room)
admin.site.register(Timetable)
admin.site.register(MyUser, UserAdmin)
