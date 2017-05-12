from django import forms
from login.models import logindatabase
from django.contrib.auth.models import User

dateformat=[
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
]

class loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}),required=True)
    loginpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'validate'}),required=True)
    remember=forms.BooleanField(required=False)

class UserForm(forms.ModelForm):
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'validate form-control'}),required=True)
    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        if  self.cleaned_data['ConfirmPassword'] != self.cleaned_data['password']:
            raise forms.ValidationError({'password':["*Passwords Don't match"]})
        return self.cleaned_data
    class Meta:
        model = User
        fields = ('first_name', 'password','last_name','email')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'validate form-control'}),
            'password':forms.PasswordInput(attrs={'class':'validate form-control'}),
            'last_name':forms.TextInput(attrs={'class':'validate form-control' }),
            'email':forms.TextInput(attrs={'class':'validate form-control' }),
            }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = logindatabase
        fields = ('Gender','Birthdate')
        widgets = {
            'Birthdate':forms.DateInput(format=dateformat,attrs={'class':'datepicker form-control','Placeholder':'Birthdate'}),
            'Gender':forms.RadioSelect(attrs={'class':'form-control','data-toggle':'radio'}),
             }

       
    
