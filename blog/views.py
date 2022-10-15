from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})
