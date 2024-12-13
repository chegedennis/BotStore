from django.shortcuts import render
from .models import Post


def blog_home(request):
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "blog/blog_home.html", {"posts": posts})


def blog_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "blog/blog_detail.html", {"post": post})
