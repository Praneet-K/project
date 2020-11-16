from django.shortcuts import render, redirect
from .models import Post
from .forms import Addpostform
from django.contrib import messages

# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,'kondeti/content.html',{'posts':posts})
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

