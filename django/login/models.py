from django.db import models
from django.contrib.auth.models import User
from django.core.validators  import RegexValidator

Gender_choices = (("MALE", "Male"),("FEMALE", "Female"),)
DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

User._meta.get_field('email')._unique = True

class logindatabase(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    Gender=models.CharField(max_length = 10,choices=Gender_choices,default="Male")
    Birthdate = models.DateField()
    def __str__(self):
        return self.user.username

