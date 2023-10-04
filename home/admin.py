from ast import Add
from django.contrib import admin
from .models import  Add_Admin, AddStudent,StudentOuting, StudentLeave, RoomChange, Complain
from .models import StudentChat
from .models import *

# Register your models here.

admin.site.register(AddStudent)
admin.site.register(Add_Admin)
admin.site.register(StudentOuting)
admin.site.register(StudentLeave)
admin.site.register(RoomChange)
admin.site.register(Complain)
admin.site.register(StudentChat)