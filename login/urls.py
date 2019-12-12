from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('mlog', views.mlog, name="mlog"),
    path('mreg', views.mreg, name="mreg"),
    path('userlogin', views.userlogin, name="userlogin")

]