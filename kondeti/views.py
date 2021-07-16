from django.shortcuts import render, redirect
from .models import Post
from .forms import Addpostform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/')
def home(request):
    posts=Post.objects.all()
    u = User.objects.all()
    return render(request,'kondeti/content.html',{'posts':posts,'u':u})

@login_required(login_url='/')
def addPost(request):
	pform = Addpostform(request.POST,request.FILES)
	if request.method == 'POST':
		if pform.is_valid():
			instance=pform.save(commit=False)
			instance.creator=request.user
			instance.save()
			messages.success(request, f'Post added')
			return redirect('/kondeti/')
	else:
		return render(request,'kondeti/addpost.html',{'pform':pform})
def display(request):
	return render(request,'kondeti/display.html',{'uname':'name'})

