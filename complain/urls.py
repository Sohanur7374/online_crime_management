from django.urls import path
from . import views

urlpatterns = [

    path('ucom', views.ucom, name="ucom")

]
