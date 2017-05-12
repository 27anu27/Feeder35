from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from adminuser.models import Student,Courses,Feedbacks,Assignment,Questions,Response
from adminuser.forms import CourseProfileForm,feedbackform,student
from login.forms import UserForm,UserProfileForm
from login.models import logindatabase
from django.forms import formset_factory
from django.core.files.storage import FileSystemStorage
import csv


samplequestions=["How was overall Courses experience","Please rate instructor teaching Method","How was Quality of slides used by instructor","Rate overall course logistics"]

def welcome(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            form = CourseProfileForm()
            feedbackforms=formset_factory(feedbackform,extra=2)
            formset=feedbackforms()
            course_registered=0
            return render(request,'adminlogin.html',{'form':form,'formset':formset,'course_registered':course_registered})
        else:
            return HttpResponseRedirect('/instructor/viewdeadline/')
        
    else:
        return HttpResponseRedirect("/login")

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect("/login")




def courseregister(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            course_registered=0
            if request.method == 'POST':
                feedbackforms=formset_factory(feedbackform,extra=2)
                formset=feedbackforms(request.POST)
                form = CourseProfileForm(request.POST)
                if form.is_valid() and formset.is_valid():
                    newcourse=form.save(commit=False)
                    newcourse.course_name=newcourse.course_name.upper()
                    newcourse.course_code=newcourse.course_code.upper()
                    newcourse.save()
                    form.save_m2m()
                    Assignment.objects.create(assignment=newcourse,assignment_submission_date=newcourse.course_midsem_date,assignment_description="Midsem Date")
                    Assignment.objects.create(assignment=newcourse,assignment_submission_date=newcourse.course_endsem_date,assignment_description="Endsem Date")
                    a=["midsem","endsem"]
                    i=0
                    for form in formset:
                        temp=form.save(commit=False)
                        temp.feedback=newcourse
                        temp.feedback_type=a[i]
                        temp.save()
                        for q in samplequestions:
                            Questions.objects.create(question_feedback=temp,question_type="rating",question=q)    
                        i=i+1
                    course_registered=1
                else:
                    print(course_registered)
                    return render(request,'adminlogin.html',{'form':form,'formset':formset,'course_registered':course_registered})
            form = CourseProfileForm()
            feedbackforms=formset_factory(feedbackform,extra=2)
            formset=feedbackforms()
            return render(request,'adminlogin.html',{'form':form,'formset':formset,'course_registered':course_registered})
        else:
            return HttpResponseRedirect('/instructor/viewdeadline/')
    else:
        return HttpResponseRedirect("/login")

def add_instructor(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            instructor_registered=0
            if request.method == 'POST':
                register=UserForm(request.POST)
                registerprofile=UserProfileForm(request.POST)
                if register.is_valid() and registerprofile.is_valid():
                    newuser=register.save(commit=False)
                    newuser.set_password(register.cleaned_data['password'])
                    newuser.username=newuser.email
                    newuser.save()
                    newuser_extra=registerprofile.save(commit=False)
                    newuser_extra.user=newuser
                    newuser_extra.save()
                    instructor_registered=1
                else:
                     return render(request,'add_instructor.html',{'register':register,'registerprofile':registerprofile,'instructor_registered':instructor_registered})
            register=UserForm()
            registerprofile=UserProfileForm()
            return render(request,'add_instructor.html',{'register':register,'registerprofile':registerprofile,'instructor_registered':instructor_registered})
        else:
            return HttpResponseRedirect('/instructor/viewdeadline/')   
    else:
        return HttpResponseRedirect("/login")   

def addstu(file):
    with open(str(file)) as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            a = Student(student_name = row[0],student_roll=row[1],student_email=row[2],student_password=row[3])
            a.save()


def add_students(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            student_added=0
            if request.method == 'POST' and request.FILES['CSVfile']:
                myfile = request.FILES['CSVfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                print(filename)
                file="media/"+filename[0:len(filename)-4]+".csv"
                addstu(file)
                student_added=1
            return render(request,'add_student.html',{'student_added':student_added})
        else:
            return HttpResponseRedirect('/instructor/viewdeadline/')  
    else:
        return HttpResponseRedirect("/login")          





        

