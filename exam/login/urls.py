from django.urls import path

from .import views

urlpatterns=[   
    path('',views.Login.as_view(),name='mainpage'),
    path('regstr',views.Regs.as_view(),name='regstr'),
    path('admins',views.Admins.as_view(),name='hello'),
   # path('approve',views.Approve.as_view(),name='approve'),
   path('change',views.forget.as_view(),name='change'),
   path('password',views.changepasswrd.as_view(),name='password')
] 