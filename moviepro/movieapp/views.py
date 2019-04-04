from django.shortcuts import render
from .models import Telugu,English,Hindhi,Userdata
from django.http import HttpResponse

def homeview(request):
    return render(request,'home.html')
def telugu(request):
    tdata=Telugu.objects.all()
    return render(request,'telugu.html',{'tdata':tdata})
def english(request):
    edata=English.objects.all()
    return render(request,'english.html',{'edata':edata})
def hindu(request):
    hdata=Hindhi.objects.all()
    return render(request,'hindhu.html',{'hdata':hdata})



def identails(request):
    if request.method == 'POST':
            moviename=request.POST.get('moviename','')
            username=request.POST.get('uname','')
            password=request.POST.get('pwd','')
            mobile=request.POST.get('mobile','')
            adharnumber=request.POST.get('adhar','')
            show=request.POST.get('show','')
            data=Userdata(
                moviename1=moviename,
                username1=username,
                password=password,
                mobile1=mobile,
                adharnumber1=adharnumber,
                showtime1=show
            )
            data.save()
            return HttpResponse("login successfully")
            #return render(request, 'user.html')
    else:
        return render(request,'user.html')