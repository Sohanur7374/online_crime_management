from django.shortcuts import render
from django.http import request

from police.models import policeregistration
from user.models import userregistration


def mlog(request):
    return render(request, 'm_log/log.html')
def mreg(request):
    return render(request, 'm_log/reg.html')

def userlogin(request):
    if request.method == 'POST':
        uselect = request.POST['userselect']
        if uselect == "User":
            mail = request.POST['uemail']
            upass = request.POST['password']
            loggedin = userregistration.objects.filter(email=mail, password=upass)
            if loggedin:
                return  render(request, 'complain/complain.html')
        else:
            mail = request.POST['uemail']
            upass = request.POST['password']
            loggedin = policeregistration.objects.filter(email=mail, password=upass)
            if loggedin:
                return render(request, 'police/dashbord.html')
