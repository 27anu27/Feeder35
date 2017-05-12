from django.db import models
from login.models import logindatabase
from django.core.validators import RegexValidator

Credit_choices = (('8','8'),('9','9'),('6','6'),('3','3'),('4','4'),)
semester_choice=(("Spring","Spring"),("Autumn","Autumn"),)
Gender_choices = (("MALE", "Male"),("FEMALE", "Female"),)
question_types=(("Textbox", "Textbox"),("Single correct", "Single Correct"),("Ratings", "Ratings"),
    ("Checkbox", "Checkbox"),("Dropdown Select", "Dropdown Select"),)

class Student(models.Model):
    student_name = models.CharField(max_length=200,blank=False,null = False)
    student_roll = models.CharField(max_length=200,blank=False,null = False,primary_key=True)
    student_email = models.CharField(max_length=200,blank=False,unique=True)
    student_branch = models.CharField(max_length=200,null = True)
    student_password=models.CharField(max_length=200,blank=False,null = False)
    student_Gender=models.CharField(max_length = 10,choices=Gender_choices,null=True)
    student_Birthdate = models.DateField(null=True)
    def __str__(self):
        return self.student_roll

class Courses(models.Model):
    course_instructor = models.OneToOneField(logindatabase,null=True)
    course_students = models.ManyToManyField(Student)
    course_venue = models.CharField(max_length = 15,blank=False,null = False)
    course_slot = models.IntegerField(blank = False,null = False)
    course_name = models.CharField(max_length = 30,blank = False,null = False)
    course_code = models.CharField(max_length = 30,blank = False,null = False,primary_key=True)
    course_semester = models.CharField(max_length = 30,choices=semester_choice,blank = False,null = False,default="spring")
    course_halfsem = models.BooleanField(default = False,blank = False,null = False)
    course_credit = models.CharField(validators=[RegexValidator(regex='^[0-9]{1,2}$',message='Please choose from the given list',code='Course credit')],max_length = 30,choices=Credit_choices,blank = False,null = False,default='6')
    course_midsem_date=models.DateField()
    course_endsem_date=models.DateField()
    def __str__(self):
        return self.course_code

class Feedbacks(models.Model):
    feedback=models.ForeignKey(Courses,on_delete=models.CASCADE)
    feedback_type=models.CharField(max_length=50,blank=False,null = False)
    feedback_submission_date=models.DateField()
    def __str__(self):
        return self.feedback_type

class Assignment(models.Model):
    assignment=models.ForeignKey(Courses,on_delete=models.CASCADE)
    assignment_submission_date=models.DateField()
    assignment_description=models.CharField(max_length=50,blank=False,null = False,unique=True)
    def __str__(self):
        return self.assignment_description

class Questions(models.Model):
    question_feedback=models.ForeignKey(Feedbacks,on_delete=models.CASCADE)
    question_type=models.CharField(max_length = 30,blank = False,null = False,default="Ratings")
    question = models.CharField(max_length = 100,blank = False,null = False)
    question_parameters = models.CharField(max_length = 150,blank=True,null = True)
    def __str__(self):
        return self.question

class Response(models.Model):
    response_question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    response_student= models.ForeignKey(Student,on_delete=models.CASCADE)
    response_answer=models.CharField(max_length=50,blank=False,null = False)
    def __str__(self):
        return self.response_answer
    class Meta:
        ordering = ('response_question',)













