from pyexpat import model
from re import M
from statistics import mode
from telnetlib import STATUS
from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AddStudent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_first_name = models.CharField(max_length=50)
    father_last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    alternate_number = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,null=True)
    blood_group = models.CharField(max_length=50, null=True)
    college_name = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    hostel = models.CharField(max_length=50, null=True)
    floor = models.CharField(max_length=50, null=True)
    room_number = models.CharField(max_length=50)
    status = models.BooleanField('Aproved', default=False)
    Aaa = models.CharField(max_length=50, null=True)
    Aab = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.first_name + ',' + self.roll_no
    
    
class StudentOuting(models.Model):
    hostel = models.CharField(max_length=25,null=True )
    room_no = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=20)
    student_name = models.CharField(max_length=50)
    outing_time = models.CharField(max_length=20)
    in_time = models.CharField(max_length=20)
    reason = models.CharField(max_length=50)
    status = models.BooleanField('Aproved', default=False)
    Aaa = models.CharField(max_length=50, default='Pending')
    Aab = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.roll_no
    
class StudentLeave(models.Model):
    hostel = models.CharField(max_length=25,null=True )
    room_no = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=20)
    student_name = models.CharField(max_length=50)
    dept = models.CharField(max_length=25)
    date_of_outing = models.CharField(max_length=20, null=True)
    date_of_comeing = models.CharField(max_length=20, null=True)
    number_of_days = models.CharField(max_length=50)
    reason = models.CharField(max_length=50, null=True)
    status = models.BooleanField('Aproved', default=False)
    Aaa = models.CharField(max_length=50, default='Pending')
    Aab = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.roll_no
class Add_Admin(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_first_name = models.CharField(max_length=50)
    father_last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    alternate_number = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,null=True)
    blood_group = models.CharField(max_length=50, null=True)
    community = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    Aaa = models.CharField(max_length=50, null=True)
    Aab = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.first_name + ',' + self.email_id
    
class RoomChange(models.Model):
    roll_number = models.CharField(max_length=50)
    hostel = models.CharField(max_length=20)
    old_room_no = models.IntegerField()
    new_room_no = models.IntegerField()
    student_name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    reasion = models.CharField(max_length=50)
    status = models.CharField(max_length=20,default="pending")
    Aaa = models.CharField(max_length=50, null=True)
    Aab = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.student_name
    
class Complain(models.Model):
    roll_number = models.CharField(max_length=50)
    hostel = models.CharField(max_length=20)
    room_no = models.IntegerField()
    student_name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    complain = models.CharField(max_length=50)
    status = models.CharField(max_length=20,default="pending")
    Aaa = models.CharField(max_length=50, null=True)
    Aab = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.roll_number
    
    
class StudentChat(models.Model):
    roll_number = models.CharField( max_length=50)
    msg = models.CharField( max_length=50)
    Aaa = models.CharField( max_length=50, null=True)
    Bbb = models.CharField( max_length=50, null=True)
    Ccc = models.CharField( max_length=50, null=True)
    
    def __str__(self):
        return self.roll_number
    

    
    