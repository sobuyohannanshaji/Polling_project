from django.urls import path
from .import views


urlpatterns=[
    # path('',views.index,name='index'),
path('register/',views.register,name='register'),
path('',views.log,name='log'),
path('userhome/<str:pk>',views.userhome,name='userhome'),
path('viewprofiel/<str:pk>',views.viewprofile,name='viewprofile'),
path('question/<str:pk>',views.questions,name='questions'),
path('option/<str:pk>',views.option,name='option'),
path('options/<str:pk>',views.options,name='options'),
path('result/<str:pk>',views.result,name='result'),
path('delquestion/<str:pk>',views.delquestion,name='delquestion'),
path('deloption/<str:pk>',views.deloption,name='deloption'),
path('logout/',views.logout,name='logout'),
]