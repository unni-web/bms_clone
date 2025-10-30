from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.
def index(request):
    # if request.user.is_authenticated:
        return render(request,'index.html')
    # else:
        # return redirect(loginuser)
def filim(request):
    if request.user.is_authenticated:
        return render(request,'filim.html')
    else:
        return redirect(loginuser)


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        data=User.objects.create_user(username=username,email=email,password=password)
        data.save()
        return redirect(loginuser)
    return render(request,'register.html')

def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(filim)
        else:
            return redirect(loginuser) 
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect(index)



def book(request):
     if request.method=='POST':
        email=request.POST['email']
        try:
            send_mail(
                subject='BOOKING CONFIRMED',
                message='Your booking for Kanthara:Chapter 1 is confirmed.',
                from_email='unnikrish1011@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request,"Booking Completed")
            return redirect (index)
        except:
                messages.error(request,"email not send")
     return render(request,'book.html')