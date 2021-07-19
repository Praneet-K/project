from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .forms import UserRegisterForm, UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.core.mail import send_mail 

# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username Taken')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email Tacken')
                return redirect('/register')
            else:
                user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save();
                # messages.success(request,'User Created login now')
                # subject = 'Registration Sucessful'
                # message = f'Hi {user.username}, thank you for registering in project.'
                # email_from = settings.EMAIL_HOST_USER 
                # recipient_list = [user.email, ] 
                # send_mail( subject, message, email_from, recipient_list )
                return redirect('/')
        else:
            messages.warning(request,'Passwords do not match')
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
            messages.warning(request,'Username or password incorrect')
            return render(request,'accounts/login.html')
    else:
        return render(request,'accounts/login.html')

@login_required(login_url='/')
def logout(request):
    auth.logout(request);
    return redirect('/')

@login_required(login_url='/')
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect("/kondeti")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/update.html', context)
