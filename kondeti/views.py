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
def display(request,userid):
	U = User.objects.filter(id=userid)
	#U = User.objects.get(id=userid)
	# print(U[0].username)
	return render(request,'kondeti/display.html',{'u':U[0]})

def displaypost(request,pk):
	p = Post.objects.get(id=pk)
	return render(request,'kondeti/displaypost.html',{'p':p})

