from django.forms import Form
from django import forms
from .models import registration
from django.forms import ModelForm

GENDER=[
    ('female','FEMALE'),('male','MALE')
]
COURSE=[
    ('python', 'PYTHON'),('java' ,'JAVA')
]


class log(Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)
    
class register(ModelForm):
    gender=forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())
    course=forms.ChoiceField(choices=COURSE, widget= forms.RadioSelect())
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = registration
        fields = ['First_name','Last_name','gender','email','course','password']
    
class forgetpassword(Form):
    Enter_mail=forms.EmailField()


class changepassword(Form):
    valid_mail=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    conform_password=forms.CharField(widget=forms.PasswordInput()) 
