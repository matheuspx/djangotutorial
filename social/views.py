# social/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Post, Like, Comment, Share

# ----------------------------
# Home / Feed principal
# ----------------------------
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "social/home.html", {"posts": posts})

# ----------------------------
# Registro de usuário
# ----------------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "social/register.html", {"form": form})

# ----------------------------
# Login
# ----------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usuário ou senha inválidos")
    else:
        form = AuthenticationForm()
    return render(request, "social/login.html", {"form": form})

# ----------------------------
# Logout
# ----------------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect("home")

# ----------------------------
# Criar Post
# ----------------------------
@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content")
        image = request.FILES.get("image")
        if content or image:
            Post.objects.create(author=request.user, content=content, image=image)
            messages.success(request, "Post criado com sucesso!")
        return redirect("home")
    return render(request, "social/create_post.html")

# ----------------------------
# Editar Post
# ----------------------------
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == "POST":
        post.content = request.POST.get("content")
        if request.FILES.get("image"):
            post.image = request.FILES.get("image")
        post.save()
        messages.success(request, "Post editado com sucesso!")
        return redirect("home")
    return render(request, "social/edit_post.html", {"post": post})

# ----------------------------
# Deletar Post
# ----------------------------
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deletado com sucesso!")
        return redirect("home")
    return render(request, "social/delete_post.html", {"post": post})

# ----------------------------
# Like / Deslike
# ----------------------------
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect("home")

# ----------------------------
# Comentar
# ----------------------------
@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(user=request.user, post=post, content=content)
            messages.success(request, "Comentário adicionado!")
    return redirect("home")

# ----------------------------
# Compartilhar
# ----------------------------
@login_required
def share_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Share.objects.create(user=request.user, post=post)
    messages.success(request, "Post compartilhado!")
    return redirect("home")