from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
import csv, io
from io import TextIOWrapper
from django.core.files.storage import FileSystemStorage
import zipfile
from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')
    pass



@login_required(login_url='/index')

def admin_dashboard(request):
    user = request.user
    

    print("user::::",str(user))
    return render(request,'admin_dashboard.html')
    pass



def admin_login_action(request):

    if request.method == "POST":
        uname = request.POST.get("uname",False)
        passwrd = request.POST.get("passwrd",False)
        print("username:::",str(uname))
        print("password:::",str(passwrd))
        user = authenticate(username=uname, password=passwrd)
        if user is not None:
            login(request, user)
            print("login success")
            return redirect("admin_dashboard")
        else:
            print("login error")
            context = {
                'message':'error'
            }
            return render(request,'index.html',context)



@login_required(login_url='/index')
def admin_add_teacher(request):

    return render(request,'add_teacher.html')


@login_required(login_url='/index')
def admin_upload_teachers_details_action(request):

    if request.method == "POST":
        csv_data = request.FILES['csv_data']
        img_data = request.FILES['img_data']
        
        data_set = csv_data.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string):
            if column[0] == '':
                    continue
            else:
                firstname = column[0]
                lastname = column[1]
                profile_pic = column[2]
                email = column[3]
                phone = column[4]
                room_no = column[5]
                subject = column[6]
                print("firstname:::",str(firstname))
                print("lastname::::",str(lastname))
                print("profile_pic:::",str(profile_pic))
                print("email::",str(email))
                print("phone:::",str(phone))
                print("Room_no::",str(room_no))
                print("subject:::::",str(subject))
                try:
                    email_alredy_exists = Teacher_details.objects.get(email=email)
                    if email_alredy_exists is not None:

                        continue
                    
                except Teacher_details.DoesNotExist:

                    subjects_list = str(subject).split(",")
                    print("subject:::::::::::::::::::----")
                    print(subjects_list)

                    teacher_save = Teacher_details.objects.create(
                        first_name=firstname,
                        email = email,
                        last_name=lastname,
                        profile_pic = "teacher_pic/"+str(profile_pic),
                        phone_number = phone,
                        room_no = room_no
                    )

                    for subject in subjects_list:
                        
                        print(subject)

                        save_subject = Teacher_subject_details(
                            teacher_id_id = teacher_save.id,
                            subject_name = str(subject)
                        )
                        save_subject.save()

                    


                    pass

                
        from zipfile import ZipFile

        with ZipFile(img_data, 'r') as zipObj:

            zipObj.extractall('media/teacher_pic/')


        return render(request,'add_teacher.html')
        
        



@login_required(login_url='/index')
def admin_view_teacher(request):

    teachers_data = Teacher_details.objects.all()
    context = {
        'teachers_data':teachers_data
    }
    return render(request,'admin_view_teacher.html',context)



def view_teacher_more_details(request):
    id = request.GET.get("id",False)
    print("id:::::::::::",str(id))
    data = Teacher_details.objects.get(id=id)
    context = {
        'data':data
    }
    return render(request,'view_teacher_more_details.html',context)


def search_result(request):

    search_data = request.GET.get("search_data")
    print("search_data:::::::::::",str(search_data))
    teachers_data = Teacher_details.objects.filter(first_name__istartswith=search_data) | Teacher_details.objects.filter(last_name__istartswith=search_data) | Teacher_details.objects.filter(tecaher_id__subject_name__istartswith=search_data)
    context = {
        'teachers_data':teachers_data
    }
    return render(request,'search_result.html',context)





def login_page(request):
    return render(request,'index.html')
