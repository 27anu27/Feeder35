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
from views import welcome,logoutuser,courseregister,add_instructor,add_students,addstu

urlpatterns = [
    url(r'^$',welcome,name='adminpage'),
    url(r'^logout/$',logoutuser,name='logout'),
    url(r'^addcourse/$',courseregister,name='courseregister'),
    url(r'^addinstructor/$',add_instructor,name='instructorregister'),
    url(r'^addstudent/$',add_students,name='studentregister'),
    url(r'^add/$',addstu,name='add'),
]
