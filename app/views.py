from django.core import paginator
from django.contrib import messages
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.shortcuts import render,redirect
from django.forms import ModelForm
from .models import Blog
from.forms import *
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator





# Create your views here.
def blog(request):
    blog = Blog.objects.all().order_by('id')
    paginator = Paginator(blog, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj':page_obj}
    return render(request,'blog.html',context)




def blog_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        creat_at = request.POST['creat_at']
        blog = Blog(title=title,description=description,creat_at=creat_at,user=request.user)
        blog.save()
        messages.info(request,'Post Has Been Submited')
        return redirect('/')
    return render(request,'blog_post.html')

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}
    return render(request,'blog_detail.html',context)


def edit(request,id):
    if request.method =='POST':
        blog = Blog.objects.get(pk=id)
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        blog = Blog.objects.get(pk=id)
        form = BlogForm(instance=blog)    
    return render(request,'edit.html',{'form':form}) 


def detele(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.info(request,'Post Has Been Deleted')
    return redirect('/')   

  



def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:

            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Is Taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Is Taken')
                return redirect('/signup') 
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                return redirect('/login')
        else:
            messages.info(request,'Password Is Not Match')
            return redirect('/signup')
    return render(request,'signup.html')



def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Cridintial') 
            return redirect('/login')   
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    return render(request,'profile.html')



  
  


