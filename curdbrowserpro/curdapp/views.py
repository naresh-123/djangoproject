from django.shortcuts import render
from .forms import Insertform,Updateform,Deleteform
from .models import Productdata
from django.http.response import HttpResponse

def homeview(request):
    return  render(request,'home.html')
def insertview(request):
    if request.method == 'POST':
        iform=Insertform(request.POST)
        if iform.is_valid():
            productnumber=request.POST.get('productnumber','')
            productname=request.POST.get('productname','')
            productcost=request.POST.get('productcost','')
            productclass=request.POST.get('productclass','')
            productweight=request.POST.get('productweight','')
            data=Productdata(
                productnumber=productnumber,
                productname=productname,
                productcost=productcost,
                productclass=productclass,
                productweight=productweight
            )
            data.save()
            iform = Insertform()
            return render(request, 'create.html', {'iform': iform})
    else:
        iform=Insertform()
        return render(request,'create.html',{'iform':iform})


def retriveview(request):
    pdata=Productdata.objects.all()
    return render(request,'retrive.html',{'pdata':pdata})


def updateview(request):
    if request.method == 'POST':
        udata=Updateform(request.POST)
        if udata.is_valid():
            productnumber=request.POST.get('productnumber','')
            productcost=request.POST.get('productcost','')
            pnum=Productdata.objects.filter(productnumber=productnumber)
            if not udata:
                return HttpResponse("invalid data")
            else:
                pnum.update(productcost=productcost)
            udata=Updateform()
            return render(request,'update.html',{'udata':udata})
    else:
        udata=Updateform()
        return render(request,'update.html',{'udata':udata})


def deleteview(request):
    if request.method == 'POST':
        ddata=Deleteform(request.POST)
        if ddata.is_valid():
            productnumber=request.POST.get('productnumber','')
            pnum=Productdata.objects.filter(productnumber=productnumber)
            if not pnum:
                return HttpResponse("product not avaliable")
            else:
                pnum.delete()
            ddata = Deleteform()
            return render(request, 'delete.html', {'ddata': ddata})
    else:
        ddata=Deleteform()
        return render(request,'delete.html',{'ddata':ddata})