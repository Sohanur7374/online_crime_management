from django.shortcuts import render
from django.http import request

from complain.models import Complain
from police.models import policeregistration
from user.models import userregistration

# Create your views here.

def preg(request):
    if request.method == "POST":
        name = request.POST['pname']
        email = request.POST['pemail']
        pas = request.POST['pswd']
        police_create = policeregistration(name=name, email=email, password=pas)
        police_create.save()
        return render(request, 'police/policeregistrattion.html')
    else:
        return render(request, 'police/policeregistrattion.html')

def viewComplain(request):
       print(111)
       complain = Complain.objects.all()
       print(222)
       return render(request, 'police/viewcomplain.html', {'complain': complain})


def viewUser(request):

    users= userregistration.objects.all()

    return render(request, 'police/viewuser.html', {'users': users})
    #return render(request, 'police/dashbord.html')
def others(request):
    return render(request, 'police/other.html')
def viewedit(request):
    editcom= Complain.object.all()

    return render(request, 'police/complainedit.html'), {'editcom': editcom}