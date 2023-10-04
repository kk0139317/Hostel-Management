from distutils.log import error
import email
from re import S
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.models import User
from .models import  Add_Admin, AddStudent, StudentOuting, StudentLeave, RoomChange, Complain, StudentChat
from django.contrib import messages
# from django.views.decorators.csrf import csrf_exemp

def s_1500(request):
    students = AddStudent.objects.filter(room_number = 1500)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1501(request):
    students = AddStudent.objects.filter(room_number = 1501)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1502(request):
    students = AddStudent.objects.filter(room_number = 1502)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1503(request):
    students = AddStudent.objects.filter(room_number = 1503)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1504(request):
    students = AddStudent.objects.filter(room_number = 1504)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1505(request):
    students = AddStudent.objects.filter(room_number = 1505)
    students = {'students':students}
    return render(request, 'students-list.html', students)


def s_1506(request):
    students = AddStudent.objects.filter(room_number = 1506)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1507(request):
    students = AddStudent.objects.filter(room_number = 1507)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1508(request):
    students = AddStudent.objects.filter(room_number = 1508)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1509(request):
    students = AddStudent.objects.filter(room_number = 1509)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1510(request):
    students = AddStudent.objects.filter(room_number = 1510)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1511(request):
    students = AddStudent.objects.filter(room_number = 1511)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1512(request):
    students = AddStudent.objects.filter(room_number = 1512)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1513(request):
    students = AddStudent.objects.filter(room_number = 1513)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1514(request):
    students = AddStudent.objects.filter(room_number = 1514)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1515(request):
    students = AddStudent.objects.filter(room_number = 1515)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1516(request):
    students = AddStudent.objects.filter(room_number = 1516)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1517(request):
    students = AddStudent.objects.filter(room_number = 1517)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1518(request):
    students = AddStudent.objects.filter(room_number = 1518)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1519(request):
    students = AddStudent.objects.filter(room_number = 1519)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1520(request):
    students = AddStudent.objects.filter(room_number = 1520)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1521(request):
    students = AddStudent.objects.filter(room_number = 1521)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1522(request):
    students = AddStudent.objects.filter(room_number = 1522)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1523(request):
    students = AddStudent.objects.filter(room_number = 1523)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1524(request):
    students = AddStudent.objects.filter(room_number = 1524)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1525(request):
    students = AddStudent.objects.filter(room_number = 1525)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1526(request):
    students = AddStudent.objects.filter(room_number = 1526)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1527(request):
    students = AddStudent.objects.filter(room_number = 1527)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1528(request):
    students = AddStudent.objects.filter(room_number = 1528)
    students = {'students':students}
    return render(request, 'students-list.html', students)

def s_1529(request):
    students = AddStudent.objects.filter(room_number = 1529)
    students = {'students':students}
    return render(request, 'students-list.html', students)
