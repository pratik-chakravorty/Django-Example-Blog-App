from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

def blog_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/blog-list.html", {"posts": posts})


def blog_detail_view(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        comment = form.cleaned_data.get('comment')
        Comment.objects.create(name=name, comment=comment, post=post)
        return redirect('blog-detail', id=post.id)
    return render(request, "posts/blog-detail.html", {"post": post, "form": form})

def blog_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog-list')
    return render(request, "posts/blog-create.html", {"form": form})

def blog_update_view(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog-list')
    
    return render(request, "posts/blog-update.html", {"form": form})

def blog_delete_view(request, id):
    Post.objects.get(id=id).delete() 
    return redirect('blog-list')
    
    

