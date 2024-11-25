from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path('',views.index,name='homepage'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutUser,name='logout'),
]
