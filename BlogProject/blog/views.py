from django.shortcuts import render, redirect
from django.db.models import Max
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models
from .forms import ContactForm, PostForm, CreateUserForms

# Create your views here.

def gethome(request):
    auth = False
    if request.user.is_authenticated:
        auth = True
        
    listPost = models.Post.objects.all()
    context = {
		'listPost': listPost,
        'auth': auth
	}
    
    return render(request, 'home.html', context)

def getAbout(request):
    auth = False
    if request.user.is_authenticated:
        auth = True
    context = {
        'auth': auth
    }
    return render(request, 'about.html', context)

def getRegister(request):
    auth = False
    formRegister = CreateUserForms()
    
    if request.user.is_authenticated:
        auth = True
        
    context = {
        'auth': auth,
        'form': formRegister
    }
    
    if request.method == 'POST':
        formGet = CreateUserForms(request.POST)
        if formGet.is_valid():
            formGet.save()
            username = formGet.cleaned_data['username']
            email = formGet.cleaned_data['email']
            password = formGet.cleaned_data['password1']
            
        else:
            contextError = {
                'auth': auth,
                'form': formRegister,
                'error': formGet.error_messages }
            return render(request, 'register.html', contextError )

    return render(request, 'register.html', context)

def getSamplePost(request):
    auth = False
    if request.user.is_authenticated:
        auth = True
    listPost = models.Post.objects.all()
    samplePost = listPost.order_by('id')[0]
    
    context = {
        'samplePost': samplePost,
        'auth': auth
    }
    
    return render(request, 'samplePost.html', context)

def getContact(request):
    auth = False
    if request.user.is_authenticated:
        auth = True
    context = {
        'auth': auth
    }
    return render(request, 'contact.html', context)

@login_required(login_url = 'blog:login')
def getWrite(request):
    if request.user.is_authenticated:
        return render(request, 'writeblog.html')

        
def getLogin(request):
    if request.user.is_authenticated:
        context = {
            'auth': True
        }
        return render(request, 'login.html', context)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        Flag = False;
        if user is not None:
            login(request, user)
            print("Login Successfully")
            Flag = True;
        else:
            print("Login UnSuccessfully")
            
        context = {
            'Flag': Flag,
            'auth': True
        }
        return render(request, 'home.html', context)
    
    return render(request, 'login.html', context = {'Auth': False})

def creatBlog(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            newPost = models.Post.objects.create(user = request.user ,title = form.cleaned_data['title'], content = form.cleaned_data['content'])
            newPost.save()
    return render(request, 'writeblog.html')

def getContactInfor(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            contactInfor = models.Contact.objects.create(name = name, email = email, phone = phone, message = message)
            contactInfor.save()
    return render(request, 'contact.html')

def detail(request, post_id):
    auth = False
    if request.user.is_authenticated:
        auth = True
    Post = models.Post.objects.get(id = post_id)
    context = {
        'Post': Post,
        'auth': auth
    }
    return render(request, 'detail.html', context)
            
def getLogout(request):
    logout(request)
    return gethome(request)