from django.shortcuts import render
from login.models import logindatabase
from django.contrib.auth import authenticate, login
from forms import loginform,UserForm,UserProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from adminuser.models import Student,Courses,Feedbacks,Assignment,Questions,Response
from adminuser.forms import CourseProfileForm,feedbackform,student
from django.forms import formset_factory
from django.core.exceptions import ObjectDoesNotExist
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt




def registerpage(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect('/adminuser')
        else:
            return HttpResponseRedirect('/instructor/viewdeadline/')
    else:
        active={'logintab':False,'registertab':True}
        registered=""
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
                register=UserForm()
                registerprofile=UserProfileForm()
                loginformobject=loginform()
                registered="You have been Registered . Please check your mail"
                return render(request,'loginpage.html',{'register':register,'registerprofile':registerprofile,'loginformobject':loginformobject,'active':active,'registered':registered})
        else:
            register=UserForm()
            registerprofile=UserProfileForm()
        loginformobject=loginform()
        return render(request,'loginpage.html',{'register':register,'registerprofile':registerprofile,'loginformobject':loginformobject,'active':active,'registered':registered})


def loginpage(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect('/adminuser')
        else:
            return HttpResponseRedirect('/instructor/viewdeadline/')
    else:
        active={'logintab':True,'registertab':False}
        accesserror=''
        if request.method == 'POST':
            loginformobject=loginform(request.POST)
            if loginformobject.is_valid():
                useraccess = authenticate(username=loginformobject.cleaned_data['username'],password=loginformobject.cleaned_data['loginpassword'])
                if useraccess:
                    if useraccess.is_active:
                        login(request, useraccess)
                        if useraccess.is_staff:
                            return HttpResponseRedirect('/adminuser')
                        else:
                            return HttpResponseRedirect('/instructor/viewdeadline')
                    else:
                        accesserror="Your account is disabled.Please contact administrator"
                        return HttpResponseRedirect("/login")
                else:
                    if accesserror == '':
                        accesserror='*Please enter valid Username and Password'
        else:
            loginformobject=loginform()
        register=UserForm()
        registerprofile=UserProfileForm()
        return render(request,'loginpage.html',{'register':register,'registerprofile':registerprofile,'loginformobject':loginformobject,'accesserror':accesserror,'active':active})


@csrf_exempt
def stud_login(request):
    response = {}
    response['name'] = ''
    response['rollno'] =''
    response['email'] =''
    response['loggedin']=False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Student.objects.get(student_roll=username,student_password=password)
            response['name'] = username
            response['rollno'] =user.student_name
            response['email'] =user.student_email
            response['loggedin']=True
            return HttpResponse(json.dumps(response), content_type="application/json")
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        response=[{"py/object": "__main__.Course", "course_instructor": "Akshay SS", "feedback": {"py/object": "__main__.Feedback", "ques": "Who are You??", "type": "Str"}, "name": "CS207"}]
        response="kachrapatti";
        return HttpResponse(response, content_type="application/json")



@csrf_exempt
def tud_login(request):
    p=""
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            #list(Student.objects.filter(student_name=username))+
            cours=list(Student.objects.get(student_roll=username).courses_set.all())
            p="{\"coursesList\":[";
            ass=[];
            feed=[];
            courses=Student.objects.get(student_roll=username).courses_set.all()
            i=0;
            j=0;
            for course in courses:
                ass=list(course.assignment_set.all())
                feed=list(course.feedbacks_set.all())
                p=p+"{\"course_instructor\":\""+str(course.course_instructor)+"\","
                p=p+"\"course_venue\":\""+str(course.course_venue)+"\","
                p=p+"\"course_slot\":\""+str(course.course_slot)+"\","
                p=p+"\"course_name\":\""+str(course.course_name)+"\","
                p=p+"\"course_code\":\""+str(course.course_code)+"\","
                p=p+"\"course_sem\":\""+str(course.course_semester)+"\","
                p=p+"\"course_credit\":\""+str(course.course_credit)+"\","
                p=p+"\"deadlines\":["
                for assv in ass:
                    p=p+"{"
                    p=p+"\"id\":\""+str(assv.assignment)+"\","
                    p=p+"\"Sub_date\":\""+str(assv.assignment_submission_date)+"\","
                    p=p+"\"type\":\""+str(assv.assignment_description)+"\""
                    p=p+"},"
                p=p[:-1]
                p=p+"],"
                p=p+"\"feedbacks\":["
                for feedv in feed:
                    p=p+"{"
                    p=p+"\"feedback_id\":\""+str(feedv.id)+"\","
                    p=p+"\"feedback_type\":\""+str(feedv.feedback_type)+"\","
                    p=p+"\"feedback_date\":\""+str(feedv.feedback_submission_date)+"\""
                    p=p+"},"
                p=p[:-1]
                p=p+"],"
                p=p[:-1]
                p=p+"},"
                i=i+1
            p=p[:-1]
            p=p+"]}"
            
            # abc.replace("\\", "")
            return HttpResponse(p, content_type="application/json")
        except ObjectDoesNotExist:
            return HttpResponse(p, content_type="application/json")
    else:
        return HttpResponse(p, content_type="application/json")


@csrf_exempt
def response_data(request):
    p=""
    if request.method == 'POST':
        response_id = request.POST.get('response_id')
        user_id=request.POST.get('student_id')
        try:
            #list(Student.objects.filter(student_name=username))+
            print response_id
            print user_id
            p="{\"questions\":["
            zlist=list(Questions.objects.filter(question_feedback__id=response_id))
            for zl in zlist:
                p=p+"{\"question_id\":\""+str(zl.id)+"\","
                p=p+"\"question\":\""+str(zl.question)+"\"},"
            p=p[:-1]
            p=p+"]}"
            return HttpResponse(p, content_type="application/json")
        except ObjectDoesNotExist:
            return HttpResponse(p, content_type="application/json")
    else:
        return HttpResponse(p, content_type="application/json")

@csrf_exempt
def answer_data(request):
    p=""
    if request.method == 'POST':
        ques_id = request.POST.get('ques_id')
        user_id=int(request.POST.get('student_id'))
        answer_array=request.POST.get('answer')
        dic={}
        dic['res']="SUCCESS"
        try:
            #list(Student.objects.filter(student_name=username))+
            queid_list = ques_id.split(",")
            n=len(queid_list)
            ans_list = answer_array.split(",")
            i=0
            student_answered=Student.objects.get(student_roll=user_id)  
            for i in range(0,n-1):
                qd=queid_list[i]
                q=int(qd)
                k=str(ans_list[i])
                l=k[0]
                print k
                print l;
                question_answered_id=Questions.objects.get(id=q)
                Response.objects.create(response_question=question_answered_id,response_student=student_answered,response_answer=l)
                i=i+1
            return HttpResponse(json.dumps(dic), content_type="application/json")
        except ObjectDoesNotExist:
            return HttpResponse(p, content_type="application/json")
    else:
        return HttpResponse(p, content_type="application/json")

  
