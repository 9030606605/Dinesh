from django.contrib import admin
from. models import registration
# Register your models here.



class Listdisplay(admin.ModelAdmin):
    list_display=['First_name','Last_name','email','gender']
    list_filter=['Last_name']


admin.site.register(registration,Listdisplay)