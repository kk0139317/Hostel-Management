from distutils.log import error
import email
from re import S
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.models import User
from .models import  Add_Admin, AddStudent, StudentOuting, StudentLeave, RoomChange, Complain, StudentChat
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        number_of_student = AddStudent.objects.count()
        number_of_admin = int(Add_Admin.objects.count())
        pending_leave = StudentLeave.objects.filter(Aaa = 'pending')
        pending_outing = StudentOuting.objects.filter(Aaa = 'Pending')
        pending_outing = pending_outing.count()
        pending_leave = pending_leave.count()
        complain = Complain.objects.filter(status='pending')
        ee = {'number_of_student': number_of_student,  'number_of_admin':number_of_admin, 
              'pending_leave':pending_leave, 'pending_outing': pending_outing,
              'complain':complain}
        
        em = request.user.email
        if em == 'Null@gmail.com':
            return render(request, 'index.html',ee  )
        else:
            return redirect('/student-index')
def profile(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        username = request.user.username
        user_admin_detail = Add_Admin.objects.filter(email_id=username)
        user_admin_detail = {'user_admin_detail':user_admin_detail}
        return render(request, 'profile.html', user_admin_detail)

def hostel(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'hostel.html')

def outing(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        username = request.user.username
        stl = StudentOuting.objects.filter(Aaa = 'Pending')
        student_outing = {'student_outing':stl}
        return render(request, 'outing.html',student_outing)

def leave(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else: 
        stl = StudentLeave.objects.filter(Aaa='pending')
        student_leave = {'student_leave':stl}
        return render(request,"leave.html", student_leave)
        

def mess(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'mess.html')

def enquiry(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'enquiry.html')

def add_new(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'add-new.html')

def add_student(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            father_first_name = request.POST.get('father_first_name')
            father_last_name = request.POST.get('father_last_name')
            mobile_number = request.POST.get('mobile_number')
            alternate_number = request.POST.get('alternate_number')
            email_id = request.POST.get('email_id')
            gender = request.POST.get('gender')
            blood_group = request.POST.get('blood_group')
            college_name = request.POST.get('college_name')
            semester = request.POST.get('semester')
            roll_no = request.POST.get('roll_no')
            dob = request.POST.get('dob')
            hostel = request.POST.get('hostel')
            floor = request.POST.get('floor')
            room_number = request.POST.get('room_number')
    
            
            studentdetail = AddStudent(first_name=first_name, last_name=last_name,
                                       father_first_name=father_first_name, father_last_name=father_last_name,
                                       mobile_number=mobile_number, alternate_number=alternate_number, 
                                    email_id=email_id, gender=gender, blood_group=blood_group,
                                    college_name=college_name, semester=semester, roll_no=roll_no, 
                                    dob=dob, hostel=hostel, floor=floor, room_number=room_number)
            
            studentdetail.save()
            user = User.objects.create_user(roll_no, email_id, dob)
            user.save()
            return redirect('/manage-student')
        else:
            return render(request,'add-student.html')
        

def breakfast(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'breakfast.html')

def complain(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        em = request.user.email
        if em == 'Null@gmail.com':
            username = request.user.username
            student_complain = Complain.objects.all()
            student_complain = {'student_complain':student_complain}
            return render(request, 'complain.html', student_complain)
        
        return render(request, 'complain.html')

def dinner(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'dinner.html')  
 
def g_floor(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'g-floor.html')

def girls_hostel(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'girls-hostel.html')

def green_hostel(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'green-hostel.html')

def hostel_1(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'hostel-1.html')

def hostel_2(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'hostel-2.html')

def hostel_3(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'hostel-3.html')

def hostel(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'hostel.html')

def lunch(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'lunch.html')

def manage_admin(request):
    adminlist = Add_Admin.objects.all()
    a = {'adminlist':adminlist}
    return render(request, 'manage-admin.html', a)

def manage_student(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        student = AddStudent.objects.all()
        s = {'student':student}
        return render(request, 'manage-student.html',s)

def add_admin(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            father_first_name = request.POST.get('father_first_name')
            father_last_name = request.POST.get('father_last_name')
            mobile_number = request.POST.get('mobile_number')
            alternate_number = request.POST.get('alternate_number')
            email_id = request.POST.get('email_id')
            gender = request.POST.get('gender')
            blood_group = request.POST.get('blood_group')
            community = request.POST.get('community')
            religion = request.POST.get('religion')
            password = request.POST.get('password')
            dob = request.POST.get('dob')
    
            Admindetail = Add_Admin(first_name=first_name, last_name=last_name,
                                       father_first_name=father_first_name, father_last_name=father_last_name,
                                       mobile_number=mobile_number, alternate_number=alternate_number, 
                                    email_id=email_id, gender=gender, blood_group=blood_group,
                                    community=community, religion=religion, password=password, 
                                    dob=dob)
            
            Admindetail.save()
            
            user = User.objects.create_user(email_id, "Null@gmail.com" , password)
            user.save()
            return redirect('manage-admin')
        else:
            return render(request, 'add-admin.html')

def room_change(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        em = request.user.email
        if em == 'Null@gmail.com':
            username = request.user.username
            room_change_en = RoomChange.objects.all()
            room_change_en = {'room_change_en':room_change_en}
            return render(request, 'room-change.html', room_change_en)
        else:
            
            return redirect('/student-index')

def update_admin(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'update-admin.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username , password=password)
        # user.login()
        if user is not None:
            login(request, user)
            em = request.user.email
            if em == 'Null@gmail.com':
                return redirect('/')
            else:
                return redirect('/student-index')
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')

# def student_index(request):
#     return render(request,"student-index.html")

def student_outing(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        if request.method == 'POST':
            username = request.user.username
            hostel = request.POST.get('hostel')
            room_no = request.POST.get('room_no')
            roll_no = username 
            student_name = request.POST.get('student_name')
            outing_time = request.POST.get('outing_time')
            in_time = request.POST.get('in_time')
            reason = request.POST.get('reason')
            
            studentouting = StudentOuting(student_name=student_name, outing_time=outing_time, 
                                         in_time=in_time, reason=reason, hostel=hostel, room_no=room_no,
                                         roll_no=roll_no)
            
            studentouting.save()
            return redirect('/student-index')
                
        else:
            return render(request,"student-outing.html")
            

def student_profile(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        username = request.user.username
        student_profile = AddStudent.objects.filter(roll_no=username)
        student_profile = {'student_profile':student_profile}
        return render(request,"student-profile.html", student_profile)

def student_leave(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        if request.method == "POST":
            hostel = request.POST.get('hostel')
            roll_no = request.user.username
            room_no = request.POST.get('room_no')
            student_name = request.POST.get('student_name')
            date_outing = request.POST.get('date_of_outing')
            date_of_comeing = request.POST.get('date_of_comeing')
            reasion = request.POST.get('reasion')
            dept = request.POST.get('dept')
            no_of_days = request.POST.get('number_of_days')
            
            
            std = StudentLeave(hostel=hostel, roll_no= roll_no , room_no=room_no, student_name=student_name
                               ,date_of_outing=date_outing, date_of_comeing=date_of_comeing, reason=reasion, dept=dept,
                               number_of_days = no_of_days, Aaa='pending')
            std.save()
            
            return redirect('/student-index')
        else:
            return render(request,"student-leave.html")


# def leave_delete(request, pid):
#     leave_form = StudentLeave.objects.get(id = pid)
#     leave_form.delete()
#     return redirect('/leave')

# def leave_accept(request, pid):
#     leave_form = StudentLeave.objects.get(id = pid)
#     leave_form.status = True
#     leave_form.save()
    
#     return redirect('/leave')



def leave_accept(request, pid):
    leave_form = StudentLeave.objects.get(id = pid)
    leave_form.Aaa = 'Aproved'
    leave_form.save()
    
    return redirect('/leave')

def leave_reject(request, pid):
    leave_form = StudentLeave.objects.get(id = pid)
    leave_form.Aaa = 'Decline'
    leave_form.save()
    return redirect('/leave')


def outing_accept(request, pid):
    leave_form = StudentOuting.objects.get(id = pid)
    leave_form.Aaa = 'Aproved'
    leave_form.save()
    
    return redirect('/outing')

def outing_reject(request, pid):
    leave_form = StudentOuting.objects.get(id = pid)
    leave_form.Aaa = 'Decline'
    leave_form.save()
    return redirect('/outing')

# def student_index(request):
#     if request.user.is_anonymous:
#         return redirect('/login')
#     else:
#         username = request.user.username
#         student_outing_status = StudentOuting.objects.filter(roll_no=username)
#         student_outing_status = {'student_outing_status':student_outing_status}
#         student_leave_status = StudentLeave.objects.filter(roll_no=username)
#         student_leave_status = {'student_leave_status':student_leave_status}
#         return render(request,"student-index.html", student_outing_status, )

def student_index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        roll_no = request.user.username
        student_det = AddStudent.objects.get(roll_no=roll_no)
        room_number = student_det.room_number
        student_s = AddStudent.objects.filter(room_number=room_number)
        your_leave_status = StudentLeave.objects.filter(roll_no=roll_no)
        pending_leave = your_leave_status.filter(Aaa = 'Pending')
        pending_leave = pending_leave.count()
        leave_accept = your_leave_status.filter(Aaa = 'Aproved')
        leave_accept = leave_accept.count() 
        leave_reject = your_leave_status.filter(Aaa = 'Decline')
        leave_reject = leave_reject.count()
        your_outing_status = StudentOuting.objects.filter(roll_no=roll_no)
        pending_outing = your_outing_status.filter(Aaa = 'pending')
        pending_outing = pending_outing.count()
        outing_accept = your_outing_status.filter(Aaa = 'Aproved')
        outing_accept = outing_accept.count() 
        outing_reject = your_outing_status.filter(Aaa = 'Decline')
        outing_reject = outing_reject.count()   
        student_s = {'student_s':student_s,'pending_leave':pending_leave,
                    'leave_accept':leave_accept, 'leave_reject':leave_reject,
                    'pending_outing':pending_outing,'outing_accept':outing_accept,
                    'outing_reject':outing_reject}
        return render(request, 'student-index.html', student_s)
    
    
def student_leave_status(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        username = request.user.username
        student_leave_status = StudentLeave.objects.filter(roll_no=username)
        student_leave_status = {'student_leave_status':student_leave_status}
        return render(request,"student-leave-status.html", student_leave_status)
    
def student_outing_status(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        username = request.user.username
        student_outing_status = StudentOuting.objects.filter(roll_no=username)
        student_outing_status = {'student_outing_status':student_outing_status}
        return render(request,"student-outing-status.html", student_outing_status)
    
def student_enquiry(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'student-enquiry.html')
    
def student_complain(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        if request.method == 'POST':
            roll_number =  request.user.username
            hostel = request.POST.get('hostel')
            room_no = request.POST.get('room_no')
            dept = request.POST.get('dept')
            complain = request.POST.get('complain')
            student_name = request.POST.get('student_name')
            
            studentcomplain = Complain(roll_number=roll_number,hostel=hostel,room_no=room_no,dept=dept,
                                       complain=complain,student_name=student_name)
            
            studentcomplain.save()
             
            return redirect('/')
        else:
            
            return render(request,'student-complain.html')
    
def student_room_change(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        if request.method == 'POST':
            username = request.user.username
            roll_no = username
            hostel = request.POST.get('hostel')
            old_room_no = request.POST.get('old_room_no')
            new_room_no = request.POST.get('new_room_no')
            student_name = request.POST.get('student_name')
            dept = request.POST.get('dept')
            reasion = request.POST.get('reasion')
            
            studentroom = RoomChange(roll_number=username, hostel=hostel, old_room_no=old_room_no,
                                              new_room_no=new_room_no, student_name=student_name, dept=dept
                                              ,reasion=reasion)
            
            studentroom.save()
            return redirect('/student-index')
        else:
            return render(request,'student-room-change.html')
    
def room_change_aproved(request, pid):
    room_change_status = RoomChange.objects.get(id = pid)
    room_change_status.status = 'Aproved'
    room_number = room_change_status.new_room_no
    roll_no = room_change_status.roll_number
    room_change_status.save()
    student_roll_no = AddStudent.objects.get(roll_no=roll_no)
    student_roll_no.room_number = room_number
    student_roll_no.save()
    
    return redirect('/room-change')

def room_change_decline(request, pid):
    room_change_status = RoomChange.objects.get(id = pid)
    room_change_status.status = 'Decline'
    room_change_status.save()
    return redirect('/room-change')

def complain_delete(request,pid):
    complain_delete = Complain.objects.get(id = pid)
    complain_delete.delete()
    return redirect('/complain')
    
def chat_student(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        em = request.user.email
        if em == 'Null@gmail.com':
            return redirect ('/')
        else:
            if request.method =='POST':
                roll_number = request.user.username
                msg = request.POST.get('msg')
                chat = StudentChat(roll_number = roll_number, msg=msg)
                chat.save()
                return redirect('/chat_student')
            else:
                roll_number = request.user.username
                others_chat = StudentChat.objects.all()
                chats = {'others_chat':others_chat }                
                return render(request, 'chat_student.html', chats)
            
def student_mess(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'student-mess.html')
    
def student_breakfast(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'student-breakfast.html')
    
def student_lunch(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'student-lunch.html')
    
def student_dinner(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'student-dinner.html')
            
