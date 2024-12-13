from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),  # Blog home page
    path("<int:post_id>/", views.blog_detail, name="blog_detail"),  # Blog detail page
]
