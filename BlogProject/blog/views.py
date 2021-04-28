from django.shortcuts import render, redirect
from django.db.models import Max
from . import models
from .forms import ContactForm, PostForm

# Create your views here.

def gethome(request):
	listPost = models.Post.objects.all()
	context = {
		'listPost': listPost
	}
	return render(request, 'home.html', context)

def getAbout(request):
	return render(request, 'about.html')

def getRegister(request):
    return render(request, 'register.html')

def getSamplePost(request):
    listPost = models.Post.objects.all()
    samplePost = listPost.order_by('id')[0]
    
    context = {
        'samplePost': samplePost
    }
    
    return render(request, 'samplePost.html', context)

def getContact(request):
	return render(request, 'contact.html')

def getWrite(request):
	return render(request, 'writeblog.html')

def getLogin(request):
    return render(request, 'login.html')

def creatBlog(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            newPost = models.Post.objects.create(title = form.cleaned_data['title'], content = form.cleaned_data['content'])
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
    Post = models.Post.objects.get(id = post_id)
    context = {
        'Post': Post
    }
    return render(request, 'detail.html', context)

def getLoginInfor(request):
    if request.user.is_authenticated:
        listPost = models.Post.objects.all()
        context = {
            'listPost': listPost
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html', context)

def getRegisterInfor(request):
    if request.user.is_authenticated:
        listPost = models.Post.objects.all()
        context = {
            'listPost': listPost
        }
        return render(request, 'home.html', context)
    else:
        