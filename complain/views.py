from django.shortcuts import render

# Create your views here.
from complain.models import Complain


def ucom(request):
    if request.method == 'POST':
        uselect = request.POST['complaintype']
        name = request.POST['name']
        phone = request.POST['phone']
        district = request.POST['district']
        thana = request.POST['thana']
        address = request.POST['address']
        discription = request.POST['discription']

        addcomplain = Complain(Complain_type=uselect, Complainant_name=name, Mobile_Number=phone, District=district, Thana
         =thana, Address=address, Complain_description=discription)
        addcomplain.save()
        return render(request, 'user/home.html')
    else:
        pass
