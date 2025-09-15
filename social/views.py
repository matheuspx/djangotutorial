# social/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment, Share

# Feed principal
@login_required
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "social/home.html", {"posts": posts})

# Criar Post
@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content")
        image = request.FILES.get("image")
        if content or image:
            Post.objects.create(author=request.user, content=content, image=image)
        return redirect("home")
    return render(request, "social/create_post.html")

# Editar Post
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == "POST":
        post.content = request.POST.get("content")
        if request.FILES.get("image"):
            post.image = request.FILES.get("image")
        post.save()
        return redirect("home")
    return render(request, "social/edit_post.html", {"post": post})

# Deletar Post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, "social/delete_post.html", {"post": post})

# Like / Deslike
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect("home")

# Comentar
@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(user=request.user, post=post, content=content)
    return redirect("home")

# Compartilhar
@login_required
def share_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Share.objects.create(user=request.user, post=post)
    return redirect("home")
