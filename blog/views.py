from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import PostForm

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog')
        
    else:
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})
