"""feeder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from views import add_assignment_deadline,input_type,add_feedback_form,view_deadline,feedbackcourseselect,feedbacknameselect

urlpatterns = [
    url(r'^adddeadline/$',add_assignment_deadline,name='add_assignment_deadline'),
    url(r'^addfeedback/$',add_feedback_form,name='add_feedback_form'),
    url(r'^inputtype/$',input_type,name='inputtype'),
    url(r'^viewdeadline/$',view_deadline,name='viewdeadline'),
    url(r'^feedbackcourse/$',feedbackcourseselect,name='feedbackcourse'),
    url(r'^feedbackname/$',feedbacknameselect,name='feedbackname'),
    # url(r'^logout/$',logoutuser,name='logout'),
    # url(r'^addcourse/$',courseregister,name='courseregister'),
    # url(r'^addinstructor/$',add_instructor,name='instructorregister'),
    # url(r'^addstudent/$',add_students,name='studentregister'),
    # url(r'^add/$',addstu,name='add'),
]