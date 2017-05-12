from django.contrib import admin

from adminuser.models import Student,Courses,Feedbacks,Assignment,Questions,Response

admin.site.register(Courses)
admin.site.register(Feedbacks)
admin.site.register(Assignment)
admin.site.register(Student)
admin.site.register(Questions)
admin.site.register(Response)

# Register your models here.
