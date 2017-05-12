from django import forms
from login.models import logindatabase
from django.contrib.auth.models import User
from adminuser.models import Student,Courses,Feedbacks,Assignment

dateformat=[
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
]

class CourseProfileForm(forms.ModelForm):
    class Meta:
        model = Courses
        exclude = ['course_instructor']
        widgets = {
        'course_midsem_date':forms.DateInput(format=dateformat,attrs={'class':'datepicker form-control'}),
        'course_endsem_date':forms.DateInput(format=dateformat,attrs={'class':'datepicker form-control'}),
        'course_venue':forms.TextInput(attrs={'placeholder':'Venue','class':'form-control'}),
        'course_name':forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
        'course_semester':forms.Select(attrs={'placeholder':'Name','class':'form-control'}),
        'course_credit':forms.Select(attrs={'placeholder':'Name','class':'form-control'}),
        'course_code':forms.TextInput(attrs={'placeholder':'Code','class':'form-control'}),
        'course_slot':forms.NumberInput(attrs={'placeholder':'Slot','class':'form-control'}),
        'course_halfsem':forms.CheckboxInput(attrs={'data-toggle':'checkbox','class':'form-control'}),
        'course_students': forms.CheckboxSelectMultiple(attrs={'data-toggle':'checkbox','class':'form-control'})
        } 

class feedbackform(forms.ModelForm):
    class Meta:
        model = Feedbacks
        exclude = ['feedback','feedback_type']
        widgets = {
        'feedback_submission_date':forms.DateInput(format=dateformat,attrs={'class':'datepicker form-control'})
        }


class feedbackform2(forms.ModelForm):
    class Meta:
        model = Feedbacks
        exclude = ['']
        widgets = {
        'feedback_submission_date':forms.DateInput(format=dateformat,attrs={'class':'datepicker form-control'}),
        'feedback_type':forms.TextInput(attrs={'placeholder':'Feedback Name','class':'form-control'}),
        'feedback':forms.Select(attrs={'placeholder':'Course name','data-toggle':'dropdown','class':'btn dropdown-toggle btn-block'}),
    }

class student(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['student_courses']
        widgets = {
        'student_Birthdate':forms.DateInput(format=dateformat,attrs={'class':'datepicker','placeholder':'Birthday'}),
        'student_Gender':forms.RadioSelect(),
        }      
        