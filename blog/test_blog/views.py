from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def home(req):
    blogs = BlogPost.objects.all()
    # return HttpResponse("Hello")
    return render(req, 'home.html',{'title': "Home",'blog': "thePythonner.tech",'blogs': blogs})

def blog(req,blog_title):
    blog = BlogPost.objects.filter(title=blog_title)[0]
    tags = blog.tag.all()
    return render(req, 'blog.html',{'title': blog.title,'blog': "thePythonner.tech",'post': blog,'tags': tags})

def create_blog(req):
    form = BlogPostForm()
    context = {
        'form': form
    }
    if req.method == 'POST':
        # print('Form Data : ', req.POST)
        form = BlogPostForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    
    return render(req, 'form.html',{'title': "Create Blog Post",'blog': "thePythonner.tech", 'form': form})
