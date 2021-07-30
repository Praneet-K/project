from django.shortcuts import render, redirect
from .models import Post,comment
from .forms import Addpostform,addCommentForm
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
	c = comment.objects.filter(post=p)
	# print(c[0])
	q={
	'p':p,
	'c':c,
	}
	return render(request,'kondeti/displaypost.html',q)

def addComment(request,pk):
	form= addCommentForm(request.POST)
	if(request.method=='POST'):
		form.comment_body=request.POST['comment_body']
		print(form.comment_body)
		instance=form.save(commit=False)
		instance.post= Post.objects.get(id=pk)
		instance.commenter_name= request.user
		instance.save()
		messages.success(request, f'Comment added')
	return redirect('kondeti:kondeti-displaypost',pk=pk)

def deletePost(request,pk):
	print('hi')
	p = Post.objects.get(id=pk)
	print(p)
	if(request.user==p.creator):
		p.delete()
		messages.success(request, f'Post deleted')
		return redirect('kondeti:kondeti-home')
	else:
		messages.warning(request,f'Post not deleted only creator can delete')
		return redirect('kondeti:kondeti-displaypost',pk=pk)

	

