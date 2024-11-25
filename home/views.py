from django.shortcuts import render,redirect
# from django.contrib.auth.models import user
from django.contrib.auth import authenticate,logout,login
# password for user is tejas$$$***000

# Create your views here.

def index(request):
    print("re",request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username, password)
        
        user = authenticate(username=username, password=password)
        print(user)
        if user:
    # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
    # No backend authenticated the credentials
            return render(request,'login.html')
    

    return render(request,'login.html')

def logoutUser(request):
    logout(request)      
    return redirect('/login')
