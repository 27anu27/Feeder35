from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from adminuser.models import Student,Courses,Feedbacks,Assignment,Questions,Response
from django.contrib.auth import authenticate, login,logout
from login.models import logindatabase
from instructor.form import assignmentdeadlineform,feedbacktypesinputform,checkboxtype,texttype,ratingtype,singlechoice,course_select,feedback_select
from django.forms import formset_factory
from adminuser.forms import feedbackform2
import datetime

def add_assignment_deadline(request):
	if request.user.is_authenticated:
		if request.user.is_staff == True:
			return HttpResponseRedirect("/adminuser")
		else:
			assignment_deadline_added=False
			if request.method == 'POST':
				form = assignmentdeadlineform(request.POST)
				if form.is_valid():   
					assignment_deadline_added=True
					form.save()
			else:
				form = assignmentdeadlineform()
		return render(request,'add_assignment_deadline.html',{'form':form,'assignment_deadline_added':assignment_deadline_added})
	else:
		return HttpResponseRedirect("/login")


def input_type(request):
	if request.user.is_authenticated:
		if request.user.is_staff == True:
			return HttpResponseRedirect("/adminuser")
		else:
			if request.method == 'POST':
				form = feedbacktypesinputform(request.POST)
				if form.is_valid():
					course_type=feedbackform2()
					ratingfeedback=formset_factory(ratingtype,extra=form.cleaned_data['input_ratings'])
					singlechoicefeedback=formset_factory(singlechoice,extra=form.cleaned_data['input_single_correct'])
					checkboxfeedback=formset_factory(checkboxtype,extra=form.cleaned_data['input_checkbox'])
					textboxfeedback=formset_factory(texttype,extra=form.cleaned_data['input_textbox'])  
					ratingfeedbackforms=ratingfeedback()
					singlechoicefeedbackforms=singlechoicefeedback()
					checkboxfeedbackforms=checkboxfeedback()
					textboxfeedbackforms=textboxfeedback() 
					return render(request,'add_feedback_form.html',{'ratingfeedbackforms':ratingfeedbackforms,'singlechoicefeedbackforms':singlechoicefeedbackforms,'checkboxfeedbackforms':checkboxfeedbackforms,'textboxfeedbackforms':textboxfeedbackforms,'course_type':course_type})
			else:
				form = feedbacktypesinputform()
		return render(request,'feedback_input_types.html',{'form':form})
	else:
		return HttpResponseRedirect("/login")

def add_feedback_form(request):
	if request.user.is_authenticated:
		if request.user.is_staff == True:
			return HttpResponseRedirect("/adminuser")
		else:
			ratingfeedback=formset_factory(ratingtype)
			singlechoicefeedback=formset_factory(singlechoice)
			checkboxfeedback=formset_factory(checkboxtype)
			textboxfeedback=formset_factory(texttype)
			course_type=feedbackform2()
			if request.method == 'POST':
				course_type=feedbackform2(request.POST)
				ratingfeedbackforms=ratingfeedback(request.POST)
				singlechoicefeedbackforms=singlechoicefeedback(request.POST)
				checkboxfeedbackforms=checkboxfeedback(request.POST)
				textboxfeedbackforms=textboxfeedback(request.POST) 
				if course_type.is_valid() and ratingfeedbackforms.is_valid() and singlechoicefeedbackforms.is_valid() and checkboxfeedbackforms.is_valid() and textboxfeedbackforms.is_valid():
					Feedback=course_type.save()
					for form in checkboxfeedbackforms:
						tempmodel=Questions.objects.create(question_feedback=Feedback,question_type="checkbox",question=form.cleaned_data['checkboxtype_question'])
						tempmodel.save()
					for form in textboxfeedbackforms:
						tempmodel=Questions.objects.create(question_feedback=Feedback,question_type="textbox",question=form.cleaned_data['texttype_question'])
						tempmodel.save()
					try:
						for form in singlechoicefeedbackforms:
							tempdata=form.cleaned_data['singlechoice_choice1']+','+form.cleaned_data['singlechoice_choice2']+','+form.cleaned_data['singlechoice_choice3']+','+form.cleaned_data['singlechoice_choice4']
							tempmodel=Questions.objects.create(question_feedback=Feedback,question_type="single_choice",question=form.cleaned_data['singlechoice_question'],question_parameters=tempdata)
							tempmodel.save()
					except:
						print("")

					try:
						for form in ratingfeedbackforms:
							tempmodel=Questions.objects.create(question_feedback=Feedback,question_type="rating",question=form.cleaned_data['ratingtype_questions'])
							tempmodel.save()
					except:
						print("")
					return HttpResponseRedirect('/instructor/inputtype')
			else:
				return render(request,'add_feedback_form.html',{'ratingfeedbackforms':ratingfeedbackforms,'singlechoicefeedbackforms':singlechoicefeedbackforms,'checkboxfeedbackforms':checkboxfeedbackforms,'textboxfeedbackforms':textboxfeedbackforms,'course_type':course_type})
	else:
		return HttpResponseRedirect("/login")


def view_deadline(request):
	if request.user.is_authenticated:
		if request.user.is_staff == True:
			return HttpResponseRedirect("/adminuser")
		else:
			Upcomingfeedbackdeadlines = Feedbacks.objects.filter(feedback_submission_date__gte=datetime.date.today())
			Oldfeedbackdeadlines = Feedbacks.objects.filter(feedback_submission_date__lt=datetime.date.today())
			Upcomingasignmentdeadlines = Assignment.objects.filter(assignment_submission_date__gte=datetime.date.today())
			Oldassignmentdeadlines = Assignment.objects.filter(assignment_submission_date__lt=datetime.date.today())
		return render(request,'view_deadlines.html',{'Upcomingasignmentdeadlines':Upcomingasignmentdeadlines,'Oldassignmentdeadlines':Oldassignmentdeadlines,'Upcomingfeedbackdeadlines':Upcomingfeedbackdeadlines,'Oldfeedbackdeadlines':Oldfeedbackdeadlines})
	else:
		return HttpResponseRedirect("/login")

def feedbackcourseselect(request):
	if request.user.is_authenticated:
		if request.user.is_staff == True:
			return HttpResponseRedirect("/adminuser")
		else:
			if request.method=='POST':
				form=course_select(request.POST)
				if form.is_valid():
					print(form.cleaned_data['course_select_name'])
					course=form.cleaned_data['course_select_name']
					feedbackname=feedback_select(initial={'feedback_select_course':course})
					feedbackname.fields["feedback_select_name"].queryset = Courses.objects.get(course_code=form.cleaned_data['course_select_name']).feedbacks_set.all()
					return render(request,'feedback_name_select.html',{'feedbackname':feedbackname})
			else:
				form=course_select()
		return render(request,'feedback_course_select.html',{'form':form})
	else:
		return HttpResponseRedirect("/login")

def feedbacknameselect(request):
	if request.user.is_authenticated:
		if request.user.is_staff == True:
			return HttpResponseRedirect("/adminuser")
		else:
			if request.method=='POST':
				form=feedback_select(request.POST)
				form.fields["feedback_select_name"].queryset = Feedbacks.objects.all()
				if form.is_valid():
					question_set=Questions.objects.filter(question_feedback__feedback_type=form.cleaned_data['feedback_select_name'],question_feedback__feedback__course_code=form.cleaned_data['feedback_select_course'])
					student_set=Courses.objects.get(course_code=form.cleaned_data['feedback_select_course']).course_students.all()
					list=[]
					for student in student_set:
						query=Response.objects.filter(response_student=student,response_question__question_feedback__feedback_type=form.cleaned_data['feedback_select_name'])
						list2=[]
						for q in query:
							list2.append(q.response_answer)
						list.append(list2)

					individual_set_aggregate=[]
					individual2_set_aggregate=[]
					response_set_aggregate=[]
					for q in question_set:
						query=Response.objects.filter(response_question__question=q,response_question__question_feedback__feedback__course_code=form.cleaned_data['feedback_select_course'],response_question__question_feedback__feedback_type=form.cleaned_data['feedback_select_name'])
						if (q.question_type == "rating"):
							list1=["1","2","3","4","5"]
							individual_set_aggregate.append(list1)
							individual2_set_aggregate.append(q.question)
							list2=[0,0,0,0,0]
							for qy in query:
								list2[int(qy.response_answer)-1]=list2[int(qy.response_answer)-1]+1
							response_set_aggregate.append(list2)
						if(q.question_type == "checkbox"):
							list1=["Yes","No"]
							individual_set_aggregate.append(list1)
							individual2_set_aggregate.append(q.question)
							list2=['0','0']
							for qz in query:
								if(qz.response_answer=="True"):
									list2[1]=str(int(list2[1])+1)
								else:
									list2[0]=str(int(list2[0])+1)	
							response_set_aggregate.append(list2)

					return render(request,'view_feedback.html',{'question_set':question_set,'list':list,'individual_set_aggregate':individual_set_aggregate,'individual2_set_aggregate':individual2_set_aggregate,'response_set_aggregate':response_set_aggregate})

			else:
				form=course_select()
		return render(request,'feedback_course_select.html',{'form':form})
	else:
		return HttpResponseRedirect("/login")
