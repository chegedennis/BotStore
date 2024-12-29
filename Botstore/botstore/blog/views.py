from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_home(request):
    posts = Post.objects.filter(status="published").order_by(
        "-published_date"
    )  # Fetch only published posts
    return render(request, "blog/blog_home.html", {"posts": posts})


def blog_detail(request, post_id):
    post = get_object_or_404(
        Post, id=post_id, status="published"
    )  # Ensure the post is published
    return render(request, "blog/blog_detail.html", {"post": post})
