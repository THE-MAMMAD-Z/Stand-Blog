from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from home.models import Contact
from django.http import HttpResponse
from .forms import TestForm,CommentForm
from django.contrib.auth.decorators import login_required

def blog(request,**kwargs):
    
    posts=Post.objects.filter(Active=1)
    if kwargs.get('auth'):
        posts=posts.filter(author__username=kwargs['auth'])
    elif kwargs.get('cat'):
        posts=posts.filter(category__name=kwargs.get('cat'))
    context={'posts':posts}
    return render(request, 'blog/blog.html',context)

@login_required
def post_details(request,num):
    
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=CommentForm()
    #post=Post.objects.get(pk=num)
    post=get_object_or_404(Post,id=num)
    comments=Comment.objects.filter(post=post,Active=1)
    return render(request, 'blog/post-details.html',{'post':post,'comments':comments,'form':form})

def search(request):
    if request.method=='GET':
        s=request.GET.get('q')
        posts=Post.objects.filter(Active=1)
        posts=posts.filter(content__contain=s)
        return render(request,'blog/blog.html',{'posts':posts})
    
def test(request):
    
    if request.method=='POST':
        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # subject=request.POST.get('subject')
        # message=request.POST.get('message')
      
        # form=TestForm(request.POST)
        # if form.is_valid():
        #     name=form.cleaned_data['name']
        #     email=form.cleaned_data['email']
        #     subject=form.cleaned_data['subject']
        #     message=form.cleaned_data['message']
        #     c=Contact()
        #     c.name=name
        #     c.email=email
        #     c.subject=subject
        #     c.message=message
        #     c.save()
        form=TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    
    form=TestForm()
    return render(request,'test.html',{'form':form})

    
    
