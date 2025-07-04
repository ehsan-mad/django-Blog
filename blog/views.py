from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Tag, Category
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView as BaseLogoutView

# Create your views here.

class LogoutView(BaseLogoutView):
    """Custom logout view that redirects to login with success message"""
    http_method_names = ['post', 'options']  # Only allow POST requests
    
    def get_success_url(self):
        return reverse_lazy('user_login') + '?logout=true'


def post_list(request):
    categoryQ = request.GET.get("category")
    tagQ = request.GET.get("tag")
    searchQ = request.GET.get("s")
    posts = Post.objects.all().order_by("-created_at")
    if categoryQ:
        posts = posts.filter(category__name=categoryQ)
    if tagQ:
        posts = posts.filter(tag__name=tagQ)
    if searchQ:
        posts = posts.filter(
            Q(title__icontains=searchQ)
            | Q(content__icontains=searchQ)
            | Q(tag__name__icontains=tagQ)
            | Q(category__name__icontains=categoryQ)
        ).distinct()

    paginator = Paginator(posts, 6)  # Increased from 2 to 6 for better UX
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page": page_obj,
        "posts": posts,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "search_query": searchQ,
        "category_query": categoryQ,
        "tag_query": tagQ,
    }
    return render(request, "blog/post_list.html", context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", id=post.id)

    else:
        form = CommentForm()
    comment = post.comment_set.all()
    is_liked = False
    if request.user.is_authenticated:
        is_liked = post.liked_post.filter(id=request.user.id).exists()
    like_count = post.liked_post.count()
    context = {
        "post": post,
        "form": form,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "comments": comment,
        "is_liked": is_liked,
        "like_count": like_count,
    }
    post.view_count += 1
    post.save()
    return render(request, "blog/post_detail.html", context)

@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.liked_post.filter(id=request.user.id).exists():
        post.liked_post.remove(request.user)
    else:
        post.liked_post.add(request.user)

    return redirect("post_detail", id=post.id)

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.author= request.user
            post.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect("post_detail", id=post.id)
    else:
        form = PostForm()
        
    return render(request, "blog/post_create.html", {"form": form})

@login_required
def post_update(request, id):
    post= get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_update.html", {"form": form})

@login_required
def post_delete(request , id):
    post= get_object_or_404(Post,id=id)
    post.delete()
    return redirect("post_list")

def user_register(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")
    else:
        form = UserCreationForm()
    return render(request, "blog/user_register.html", {"form": form})
