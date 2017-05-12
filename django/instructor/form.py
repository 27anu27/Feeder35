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

formtypes=(("Textbox", "Textbox"),
    ("Single correct", "Single Correct"),("Ratings", "Ratings"),
    ("Checkbox", "Checkbox"),)
rating_choices=(("Very Poor", "Very Poor"),
    ("Poor", "Poor"),("Average", "Average"),
    ("Good", "Good"),("Very Good", "Very Good"),)

class assignmentdeadlineform(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['']
        widgets = {
        'assignment':forms.Select(attrs={'placeholder':'Code','data-toggle':'dropdown','class':'btn dropdown-toggle btn-block'}),
		'assignment_submission_date':forms.DateInput(format=dateformat,attrs={'class':'datepicker form-control'}),
        'assignment_description':forms.Textarea(attrs={'placeholder':'Enter a description :Max 50 words','class':'datepicker form-control'})
        }

class feedbacktypesinputform(forms.Form):
    input_textbox=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Text Questions','class':'form-control'}))
    input_single_correct=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Single Correct Questions','class':'form-control'}))
    input_ratings=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Rating questions','class':'form-control'}))
    input_checkbox=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Checkbox Questions','class':'form-control'}))


class checkboxtype(forms.Form):
    checkboxtype_question=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Checkbox Type','class':'form-control'}))

class ratingtype(forms.Form):
    ratingtype_questions=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rating Type','class':'form-control'}))

class texttype(forms.Form):
    texttype_question=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Descriptive','class':'form-control'}))

class singlechoice(forms.Form):
    singlechoice_question=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Single Choice','class':'form-control'}))
    singlechoice_choice1=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Choice 1','class':'form-control'}))
    singlechoice_choice2=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Choice 2','class':'form-control'}))
    singlechoice_choice3=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Choice 3','class':'form-control'}))
    singlechoice_choice4=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Choice 4','class':'form-control'}))

class course_select(forms.Form):
    course_select_name = forms.ModelChoiceField(queryset=Courses.objects.all(),widget=forms.Select(attrs={'placeholder':'Code','data-toggle':'dropdown','class':'btn dropdown-toggle btn-block'})) 

class feedback_select(forms.Form):
    feedback_select_name = forms.ModelChoiceField(queryset=Feedbacks.objects.none(),widget=forms.Select(attrs={'placeholder':'Code','data-toggle':'dropdown','class':'btn dropdown-toggle btn-block'}))
    feedback_select_course=forms.CharField(widget=forms.HiddenInput())


