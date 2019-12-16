from django.http import request
from django.shortcuts import render

from user.models import userregistration


def index(request):
    return render(request, 'user/home.html')

def dashboard(request):
    return  render(request, 'user/dashboard.html')

def userbase(request):
    return render(request, 'user/userbase.html')
def ureg(request):
    if request.method == "POST":
        name = request.POST['uname']
        email = request.POST['email']
        pas = request.POST['pswd']
        user_create = userregistration(name=name, email=email, password=pas)
        user_create.save()
        return render(request, 'm_log/log.html')
    else:
        return render(request, 'user/registration.html')
