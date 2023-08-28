from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def login(request):


    #if request.user.is_authenticated and request.path == reverse('login'):
    # if 'username' in request.session and request.session['username'] != "":
    #         return redirect('home')
    # else:
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        print(username,pass1)
        user =authenticate(request,username=username,password=pass1)
        if user is not None:
            print(user)
                    #login(request,user)
            request.session['username'] = username
            return  redirect("/listofResume/")
                
        else:
            return HttpResponse("pls enter correct username")
 
    return render(request,'login.html')


def signup(request):
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            print(uname,email,mobile,pass1,pass2)

            if pass1 !=pass2:
                return HttpResponse("Password Not Match..")
            else:
                myuser= User.objects.create_user(uname,email,pass1)
                myuser.save()
                return redirect("/listofResume/")
            
            #HttpResponse("details Submitted successfully")

        return render(request,'signup.html')


@login_required(login_url='')
def home(request):
  username=request.session['username'] 
  username="prasad"
  #username  = request.GET.get('username')

  return render(request,"newform.html")

LOGOUT_REDIRECT_URL = 'http://127.0.0.1:8000/listofResume/' 

def logout(request):
    logout(request)
    return redirect('/login')
    #  del request.session['username']
    #  return redirect('http://127.0.0.1:8000')

    