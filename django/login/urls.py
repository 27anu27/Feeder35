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
from django.conf.urls import url
from login.views import loginpage,registerpage,stud_login,tud_login,response_data,answer_data

urlpatterns = [
    url(r'^$',loginpage,name='login'),
    url(r'^register/$',registerpage,name='registerpage'),
    url(r'^android/$',stud_login,name='androidlogin'),
    url(r'^courses/$',tud_login,name='alogin'),
    url(r'^question/$',response_data,name='alogin1'),
    url(r'^answer/$',answer_data,name='alogout'),
]
