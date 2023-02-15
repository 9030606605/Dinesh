from django.db import models


# Create your models here.
GENDER=[
    ('female', 'FEMALE'),('male', 'MALE')
]
COURSE=[
    ('python', 'PYTHON'),('java' ,'JAVA')    
]


class registration(models.Model):
    First_name=models.CharField(max_length=25)
    Last_name=models.CharField(max_length=25)
    email=models.EmailField(max_length=54)
    password=models.CharField(max_length=25,default=True)
    status=models.CharField(max_length=25,default='pending')
    gender=models.CharField(max_length=25,choices=GENDER,default=True)
    course=models.CharField(max_length=25,choices=COURSE,default=True)

    def __str__(self):
        return (self.First_name) 
