"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.homepage, name="WelcomeHome"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('userhome/', views.userhome, name="userhome"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('viewusers/', views.viewusers, name="viewusers"),
    path('signup/', views.signup, name="signup"),
    path('usignupaction/', views.usignupaction, name="usignupaction"),
    path('searchusers/', views.searchusers, name="searchusers"),
    path('ulogin/', views.ulogin, name="ulogin"),
    path('userloginaction/', views.userloginaction, name="userloginaction"),

    
    path('nntrain/', views.nntrain, name="nntrain"),
    path('svmtrain/', views.svmtrain, name="svmtrain"),
    path('knntrain/', views.knntrain, name="knntrain"),
    path('nbtrain/', views.nbtrain, name="nbtrain"),
    path('rftrain/', views.rftrain, name="rftrain"),
    path('testing/', views.testing, name="testing"),
    path('test/', views.test, name="test"),       
    path('viewacc/', views.viewacc, name="viewacc"),       
    path('prediction/', views.prediction, name="prediction"),       
    path('predictionact/', views.predictionact, name="predictionact"),       
    
    path('userlogout/', views.userlogout, name="userlogout"),
    path('viewp/', views.viewp, name="viewp"),
    path('training/', views.training, name="training"),
    path('addq/', views.addq, name="addq"),
    path('addquery/', views.addquery, name="addquery"),

    path('adddata/', views.adddata, name="adddata"),
    path('addt/', views.addt, name="addt"),
    path('chatpage/', views.chatpage, name="chatpage"),
    path('chataction/', views.chataction, name="chataction"),
    path('moredetails/', views.moredetails, name="moredetails"),

    
    

   
]
