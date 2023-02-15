from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .forms import register,log,forgetpassword,changepassword
from .models import registration
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
class Login(View):
    def get(self,request):
        context={}
        obj=log()
        context['regform']=obj
        return render (request,'login.html',context)
         
    def post(self,request):
        obj=log(request.POST)
        if obj.is_valid():
            user=obj.cleaned_data['username']
            paswrd=obj.cleaned_data['password']
            try:
                objtt=registration.objects.get(email=user,password=paswrd)
                if objtt != False:
                    return HttpResponse('srii')

            except:
                return HttpResponse('data ledhyraa')
        
       # return HttpResponse('user form')

class Regs(View):
    def get(self,request):
        context={}
        obj=register()
        context['regs']=obj
        
        return render(request,'register.html',context)

    def post(self,request):
        obj=register(request.POST)
        if obj.is_valid():
            obj.save()
            message='Admin'
            body= f"{obj.cleaned_data['First_name']} waiting  "
            mail=settings.EMAIL_HOST_USER
            res=[obj.cleaned_data['email']]
           
            send_mail(message,body,mail,res)
            return HttpResponse('register successfull')



class Admins(View):
    def get (self,request): 
        context={}
        obj=registration.objects.all()
        
        context['admins']=obj 
        return render (request,'admin.html',context)


    def post(self,request):
        app=request.POST['app']
        print(app)
        if (app=='Approves'):
                registration.objects.get(First_name=request.POST['check'])
                obj=registration.objects.filter(request.POST['check'])
                obj1=User.objects.create_user(email=obj.email,password=obj.password)
                obj1.save()
                return HttpResponse('sri')

    

'''class Approve(View):
    def get(self,request):
        if registration.objects.filter(status='pending'):

            return render (request,'admins.html')



    def post(self,request):
        app=request.POST['app']
        if (app=='Approves'):
                registration.objects.get(id=request.POST['check']).update(status='approved')
                obj=registration.objects.get(request.POST['check'])
                obj1=User.objects.create_user(email=obj.email,password=obj.password)
                obj1.save()

           
                return HttpResponse('you are approved')
            
            

        else:
            return HttpResponse('no data')'''

class forget(View):
    def get(self,request):
        context={}
        obj=forgetpassword()
        context['forget']=obj
        return render (request,'forget.html',context)
    def post(self,request):
        forget_data=forgetpassword(request.POST)
        if forget_data.is_valid():
            forgetmail_pass=forget_data.cleaned_data['Enter_mail']
            try:
                details=registration.objects.get(email=forgetmail_pass)
        
                mail=details.email
                pas=details.password
                sub='django forget mail'
                mes=f"for v cube email {mail} password{pas}"
                email_from=settings.EMAIL_HOST_USER
                reciver=[forgetmail_pass,]
                send_mail(sub,mes,email_from,reciver) 
                return redirect('mainpage')
            except:

                return HttpResponse('hello')


class changepasswrd(View):
    def get(self,request):
        context={}
        obj=changepassword()
        context['password']=obj
        return render(request,'change.html',context)
    def post(self,request):
        get=changepassword(request.POST)
        if get.is_valid():
            mail=get.cleaned_data['valid_mail']
            pas=get.cleaned_data['password']
            cpas=get.cleaned_data['conform_password']
            if pas==cpas:
                try:
                    obj=registration.objects.get(email=mail)
                    obj.password=pas
                    obj.save()
                    return HttpResponse('saved')
                except:
                    return HttpResponse('none')
            else:
                return HttpResponse('password vallidation is wrong')

           