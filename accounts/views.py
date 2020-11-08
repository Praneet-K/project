from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .forms import UserRegisterForm, UserUpdateForm , ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
    
        user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
        user.save();
        print('usercreated')
        return redirect('/')

    else:
        return render(request, 'accounts/register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("kondeti/")
    else:
        return render(request,'accounts/login.html')
def logout(request):
    auth.logout(request);
    return redirect('/')

